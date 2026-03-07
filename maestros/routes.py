import forms
from . import maestros
from flask import render_template, request, redirect, url_for
from models import Maestros, db, Curso

@maestros.route("/maestros/listado", methods=['GET', 'POST'])
def maestros_listado():
    create_form = forms.MaestroForm(request.form)
    maestros_list = Maestros.query.all()
    return render_template(
        "maestros/listadoMest.html",
        form=create_form,
        maestros=maestros_list
    )

@maestros.route("/maestros/detalle", methods=['GET'])
def detalles_maestro():
    id_req = request.args.get('id')
    
    # Buscamos al maestro. 
    # Al usar .first(), traemos el objeto que ya contiene la relación 'cursos'
    maes = Maestros.query.filter_by(matricula=id_req).first()
    
    if not maes:
        return f"Error: No existe el maestro con matrícula {id_req}", 404

    # GRACIAS A TU MODELO: No necesitas Curso.query.filter_by...
    # Solo pasamos 'maes.cursos' directamente al template.
    return render_template('maestros/detalle.html', 
                            id=maes.matricula, 
                            nombre=maes.nombre, 
                            apellidos=maes.apellidos, 
                            especialidad=maes.especialidad, 
                            email=maes.email,
                            cursos=maes.cursos) # Aquí está la magia de la relación


@maestros.route('/maestros/agregar', methods=['GET', 'POST'])
def maestros_form():
    create_form = forms.MaestroForm(request.form)
    if request.method == 'POST':
        maes = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
        )
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for('maestros.maestros_listado'))
    return render_template("maestros/Maestros.html", form=create_form)

@maestros.route('/maestros/editar', methods=['GET', 'POST'])
def modificar_maestro():
    create_form = forms.MaestroForm(request.form)
    if request.method == 'GET':
        id_req = request.args.get('id')
        maes = db.session.query(Maestros).filter(Maestros.matricula == id_req).first()
        
        if maes:
            create_form.id.data = maes.matricula
            create_form.nombre.data = maes.nombre
            create_form.apellidos.data = maes.apellidos
            create_form.email.data = maes.email
            create_form.especialidad.data = maes.especialidad
        else:
            return "Maestro no encontrado", 404

    if request.method == 'POST':
        id_req = request.form.get('id')
        maes = db.session.query(Maestros).filter(Maestros.matricula == id_req).first()
        
        if maes:
            maes.nombre = create_form.nombre.data
            maes.apellidos = create_form.apellidos.data
            maes.email = create_form.email.data
            maes.especialidad = create_form.especialidad.data
            db.session.commit()
            return redirect(url_for('maestros.maestros_listado'))

    return render_template("maestros/editar.html", form=create_form)


@maestros.route('/maestros/borrar', methods=['GET', 'POST'])
def eliminar_maestro():
    create_form = forms.MaestroForm(request.form)
    
    if request.method == 'GET':
        id_req = request.args.get('id')
        maes = db.session.query(Maestros).filter(Maestros.matricula == id_req).first()
        
        if maes:
            create_form.id.data = maes.matricula
            create_form.nombre.data = maes.nombre
            create_form.apellidos.data = maes.apellidos
        else:
            return "Maestro no encontrado", 404

    if request.method == 'POST':
        id_req = request.form.get('id')
        maes = db.session.query(Maestros).filter(Maestros.matricula == id_req).first()
        
        if maes:
            db.session.delete(maes)
            db.session.commit()
            return redirect(url_for('maestros.maestros_listado'))
            
    return render_template("maestros/borrar.html", form=create_form)


@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"perfil de {nombre}"