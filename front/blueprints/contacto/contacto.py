from flask import Blueprint, render_template
import os

contacto_bp = Blueprint("contacto_bp",__name__)

@contacto_bp.route('/contacto')
def contacto():
    return render_template('contacto.html')
