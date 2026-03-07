from flask import render_template, request, redirect, url_for
from . import inscripciones
from models import db, Alumnos, Curso, Inscripcion
from flask import flash, redirect, url_for 
from sqlalchemy.exc import IntegrityError

@inscripciones.route('/inscribirCurso', methods=['GET', 'POST'])
def inscribirCurso():
    alumno_id = request.args.get('id')
    alumno_obj = Alumnos.query.get(alumno_id)
    
    if request.method == 'POST':
        curso_id = request.form.get('curso_id')
        
        nueva_inscripcion = Inscripcion(
            alumno_id=alumno_id,
            curso_id=curso_id
        )

        try:
            db.session.add(nueva_inscripcion)
            db.session.commit()
            flash("¡Inscripción realizada con éxito!", "success")
            return redirect(url_for('alumnos.index'))
        except IntegrityError:
            db.session.rollback()  
            flash("Este alumno ya está inscrito en ese curso.", "danger")
            return redirect(url_for('alumnos.index'))

    cursos = Curso.query.all()
    return render_template("cursos/inscribirCurso.html", 
                           cursos=cursos, 
                           alumno=alumno_obj, 
                           alumno_id=alumno_id)

@inscripciones.route('/listadoInscripciones')
def listadoInscripciones():
    todas_las_inscripciones = Inscripcion.query.all()
    return render_template("cursos/listadoInscripciones.html", inscripciones=todas_las_inscripciones)

@inscripciones.route('/eliminar_inscripcion/<int:id>')
def eliminar_inscripcion(id):
    inscripcion = Inscripcion.query.get_or_404(id)
    try:
        db.session.delete(inscripcion)
        db.session.commit()
        flash("Alumno dado de baja del curso correctamente", "success")
    except Exception as e:
        db.session.rollback()
        flash("Error al dar de baja: " + str(e), "danger")
    
    return redirect(url_for('inscripciones.listadoInscripciones'))