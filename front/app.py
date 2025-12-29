from flask import Flask, render_template
from dotenv import load_dotenv
import os

from blueprints.index.index import index_bp
from blueprints.contacto.contacto import contacto_bp
from blueprints.mis_proyectos.mis_proyectos import mis_proyectos_bp
from blueprints.login.login import login_bp
from blueprints.registrarse.registrarse import registrarse_bp
from blueprints.env.env import config_mail, back_url


load_dotenv()
app = Flask(__name__)

config_mail(app)
back_url(app)


app.register_blueprint(index_bp, url_prefix="/")
app.register_blueprint(contacto_bp, url_prefix="/contacto")
app.register_blueprint(mis_proyectos_bp, url_prefix="/mis_proyectos")
app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(registrarse_bp, url_prefix="/registrarse")


if __name__  == "__main__":
    app.run("localhost", port= "5003", debug=True)