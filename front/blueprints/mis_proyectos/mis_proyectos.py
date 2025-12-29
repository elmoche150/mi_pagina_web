from flask import Blueprint, render_template
import os

mis_proyectos_bp = Blueprint("mis_proyectos_bp",__name__)

@mis_proyectos_bp.route('/')
def mis_proyectos():
    return render_template('mis_proyectos.html')