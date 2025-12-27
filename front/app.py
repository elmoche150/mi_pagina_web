from flask import Flask, render_template
from dotenv import load_dotenv
import os

from blueprints.index.index import index_bp
from blueprints.contacto.contacto import contacto_bp
from blueprints.env.env import config_mail


load_dotenv()
app = Flask(__name__)
config_mail(app)



app.register_blueprint(index_bp, url_prefix="/")
app.register_blueprint(contacto_bp, url_prefix="/contacto")


if __name__  == "__main__":
    app.run("localhost", port= "5003", debug=True)