from flask import Blueprint, url_for,request,redirect,render_template,jsonify,current_app
import requests

registrarse_bp = Blueprint("registrarse_bp",__name__)

@registrarse_bp.route('/', methods=['GET','POST'])
def registrarse():

    BACK_URL = current_app.config['BACK_URL']
    title="Registrarse"

    if request.method == 'GET':
        return render_template('registrarse.html', titulo=title)
    
    if request.method == 'POST':
        errores = []

        nombre = request.form.get('nombre')
        email = request.form.get('email')
        email_confirmacion = request.form.get('email_confirmacion')
        contrasena = request.form.get('contrasena')
        contrasena_confirmacion = request.form.get('contrasena_confirmacion')
        
        if (not nombre) or (not email) or (not email_confirmacion) or (not contrasena)or (not contrasena_confirmacion):
            errores.append("FALTAN CAMPOS")
        
        if  (email != email_confirmacion):
            errores.append("LOS EMAILS NO COINCIDEN")
        
        if  (contrasena != contrasena_confirmacion):
            errores.append("LAS CONTRASEÑAS NO COINCIDEN")

        if errores:
            return render_template('registrarse.html', titulo=title, errores=errores)
        
        data = {"nombre":nombre,"email":email,"contrasena":contrasena}
        requests.post(f"{BACK_URL}/registrarse/registrar", json=data)

    return redirect(url_for('index_bp.index'))
