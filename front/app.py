from flask import Flask, render_template
import os

from blueprints.index.index import index_bp

app = Flask(__name__)


app.register_blueprint(index_bp, url_prefix="/")


if __name__  == "__main__":
    app.run("localhost", port= "5003", debug=True)