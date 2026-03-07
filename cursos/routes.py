import forms
from flask import render_template, request, redirect, url_for, flash
from models import db, Curso, Maestros, Alumnos
from forms import CursoForm, InscripcionForm
from . import cursos


@cursos.route("/cursos/listado", methods=['GET', 'POST'])
def cursos_listado(): 
    create_form = forms.CursoForm(request.form)
    cursos_list = Curso.query.all() 
    
    return render_template(
        "cursos/listadoCurso.html", 
        form=create_form,
        cursos=cursos_list 
    )

@cursos.route("/cursos/detalle", methods=['GET'])
def detalles_curso():
    id_req = request.args.get('id')

    cur = Curso.query.filter_by(id=id_req).first()

    if not cur:
        return f"Error: No existe el curso con ID {id_req}", 404

    return render_template('cursos/detalle.html', curso=cur)

@cursos.route('/cursos/agregar', methods=['GET', 'POST'])
def cursos_form():
    create_form = forms.CursoForm(request.form)
    maestros_disponibles = Maestros.query.all() 

    if request.method == 'POST' and create_form.validate():
        nuevo_curso = Curso(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestro_id=create_form.maestro_id.data
        )
        db.session.add(nuevo_curso)
        db.session.commit()
        return redirect(url_for('cursos.cursos_listado'))
    
    if request.method == 'POST':
        print(create_form.errors)
        
    return render_template("cursos/Cursos.html", form=create_form, maestros_list=maestros_disponibles)

@cursos.route('/cursos/editar', methods=['GET', 'POST'])
def modificar_curso():
    create_form = forms.CursoForm(request.form)
    
    
    maestros_disponibles = Maestros.query.all()
    create_form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in maestros_disponibles]

    if request.method == 'GET':
        id_req = request.args.get('id')
        cur = Curso.query.get(id_req)
        
        if cur:
            create_form.id.data = cur.id
            create_form.nombre.data = cur.nombre
            create_form.descripcion.data = cur.descripcion
            create_form.maestro_id.data = cur.maestro_id
        else:
            return "Curso no encontrado", 404

    if request.method == 'POST':
        id_req = request.form.get('id')
        cur = Curso.query.get(id_req)
        
        if cur:
            cur.nombre = create_form.nombre.data
            cur.descripcion = create_form.descripcion.data
            cur.maestro_id = create_form.maestro_id.data
            db.session.commit()
            return redirect(url_for('cursos.cursos_listado'))

    return render_template("cursos/editar.html", form=create_form)


@cursos.route('/cursos/borrar', methods=['GET', 'POST'])
def eliminar_curso():
    
    create_form = forms.CursoForm(request.form)
    
    if request.method == 'GET':
        id_req = request.args.get('id')
        cur = Curso.query.get(id_req)
        
        if cur:
            create_form.id.data = cur.id
            create_form.nombre.data = cur.nombre
        else:
            return "Curso no encontrado", 404

    if request.method == 'POST':
        id_req = request.form.get('id')
        cur = Curso.query.get(id_req)
        
        if cur:
            db.session.delete(cur)
            db.session.commit()
            return redirect(url_for('cursos.cursos_listado'))
            
    return render_template("cursos/borrar.html", form=create_form)

