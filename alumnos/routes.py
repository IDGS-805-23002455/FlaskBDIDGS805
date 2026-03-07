import forms
from . import alumnos
from flask import render_template, request, redirect, url_for
from models import Alumnos, db
from alumnos import alumnos

@alumnos.route("/",methods=['GET','POST'])
@alumnos.route("/index")
def index():
    create_form = forms.UserForm(request.form)
    alumnos_lista = Alumnos.query.all()
    return render_template("alumnos/index.html", form=create_form, alumnos=alumnos_lista)

@alumnos.route('/Alumnos', methods=['GET','POST'])
def alumnos_form():
	create_form=forms.UserForm(request.form)
	if request.method == 'POST':
		alum =Alumnos(nombre=create_form.nombre.data,
					  apellidos=create_form.apellidos.data,
					  email=create_form.email.data,
       				  telefono=create_form.telefono.data,)
		db.session.add(alum)
		db.session.commit()
		return redirect(url_for('alumnos.index'))
	return render_template("alumnos/Alumnos.html", form=create_form)

@alumnos.route("/detalles", methods=['GET','POST'])
def detalles():
    if request.method=='GET':
        id=request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        nombre = alum1.nombre
        apellidos = alum1.apellidos
        email = alum1.email
        telefono = alum1.telefono
        cursos = alum1.cursos   
    return render_template(
        'alumnos/detalles.html',
        id=id,
        nombre=nombre,
        apellidos=apellidos,
        email=email,
        telefono=telefono,
        cursos=cursos   # ← ENVIAR CURSOS AL HTML
    )
    
@alumnos.route('/modificar', methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        if not id:
            return redirect(url_for('alumnos.index'))
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == int(id)).first()
        if not alum1:
            return redirect(url_for('alumnos.index'))
        create_form.id.data = alum1.id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.email.data = alum1.email
        create_form.telefono.data = alum1.telefono 


    if request.method == 'POST':
        id = create_form.id.data   
        alum = db.session.query(Alumnos).filter(Alumnos.id == int(id)).first()
        if alum:
            alum.nombre = create_form.nombre.data
            alum.apellidos = create_form.apellidos.data
            alum.email = create_form.email.data
            alum.telefono = create_form.telefono.data
            db.session.commit()
        return redirect(url_for('alumnos.index'))
    return render_template("alumnos/modificar.html", form=create_form)

@alumnos.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        if not id:
            return redirect(url_for('alumnos.index'))
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == int(id)).first()
        if alum1:
            create_form.id.data = alum1.id
            create_form.nombre.data = alum1.nombre
            create_form.apellidos.data = alum1.apellidos
            create_form.email.data = alum1.email
            create_form.telefono.data = alum1.telefono
    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == int(id)).first()
        if alum:
            db.session.delete(alum)
            db.session.commit()
        return redirect(url_for('alumnos.index'))
    return render_template("alumnos/eliminar.html", form=create_form)

@alumnos.route('/perfil/<nombre>')
def perfil(nombre):
    return f"perfil de {nombre}"