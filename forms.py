from wtforms import Form
from wtforms import IntegerField,StringField,PasswordField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id = IntegerField("id", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, max=10000, message="Ingrese valor valido")
    ])
    
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=20, message="Ingrese nombre valido")
    ])

    # Se cambió 'apaterno' por 'apellidos' para coincidir con tu HTML
    apellidos = StringField("Apellidos", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=50, message="Ingrese apellidos válidos")
    ])
    
    email = EmailField("Correo", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="Ingrese un correo valido")
    ])

    # Nuevo campo de teléfono añadido
    telefono = StringField("Teléfono", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=10, max=15, message="Ingrese un teléfono válido")
    ])