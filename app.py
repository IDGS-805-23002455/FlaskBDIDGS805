from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from config import DevelopmentConfig
from maestros import maestros
from alumnos import alumnos
from cursos import cursos
from inscripciones import inscripciones
from models import db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

app.register_blueprint(maestros)
app.register_blueprint(alumnos)
app.register_blueprint(cursos)
app.register_blueprint(inscripciones)


@app.errorhandler(404) 
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)