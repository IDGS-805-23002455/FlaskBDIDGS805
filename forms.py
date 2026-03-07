from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,PasswordField, SelectField, TextAreaField
from wtforms import EmailField
from wtforms import validators
from flask_wtf import FlaskForm
from wtforms import validators


from wtforms import StringField, IntegerField, TextAreaField, validators
from wtforms.validators import Optional 

class UserForm(FlaskForm):
    id = IntegerField("id", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, max=10000, message="Ingrese valor valido")
    ])
    
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=20, message="Ingrese nombre valido")
    ])

    apellidos = StringField("Apellidos", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=50, message="Ingrese apellidos válidos")
    ])
    
    email = EmailField("Correo", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="Ingrese un correo valido")
    ])

    telefono = StringField("Teléfono", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=10, max=15, message="Ingrese un teléfono válido")
    ])
    


class MaestroForm(FlaskForm):
    id = IntegerField("matricula", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, max=10000, message="Ingrese valor valido")
    ])
    
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=20, message="Ingrese nombre valido")
    ])

    apellidos = StringField("Apellidos", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=50, message="Ingrese apellidos válidos")
    ])
    
    especialidad = StringField("Especialidad", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=50, message="Ingrese un correo valido")
    ])
    
    email = EmailField("Correo", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="Ingrese un correo valido")
    ])
    


class CursoForm(FlaskForm):
    id = IntegerField("ID Curso", validators=[Optional()])
    
    nombre = StringField("Nombre del Curso", [
        validators.DataRequired(message="El nombre es requerido"),
        validators.length(min=4, max=150, message="Longitud no válida")
    ])

    descripcion = TextAreaField("Descripción del Curso", [
        validators.DataRequired(message="La descripción es requerida")
    ])
    
    maestro_id = StringField("Maestro Asignado", [
        validators.DataRequired(message="Debe asignar un maestro")
    ])


class InscripcionForm(FlaskForm):
    # ID autoincremental (Opcional en el form)
    id = IntegerField("ID Inscripción", validators=[Optional()])
    
    # Estos recibirán el ID desde el JavaScript del HTML
    alumno_id = StringField("Alumno", [
        validators.DataRequired(message="Debe seleccionar un alumno")
    ])
    
    curso_id = StringField("Curso", [
        validators.DataRequired(message="Debe seleccionar un curso")
    ])

