from flask import Blueprint, render_template, request, jsonify
from blueprints.env.env import mail
from flask_mail import Message
import os

contacto_bp = Blueprint("contacto_bp",__name__)

@contacto_bp.route('/', methods=['GET','POST'])
def contacto():
     
    if request.method == 'POST':
        nombre = request.form.get('nombre_usuario')
        apellido = request.form.get('apellido_usuario')
        email_usuario = request.form.get('email_usuario')
        telefono = request.form.get('telefono_usuario')
        mensaje = request.form.get('mensaje_usuario')

        try:

            # Mail para el administrador
            msg_admin = Message(
                subject=f"Nuevo mensaje de El Portafolio de {nombre} {apellido}",
                recipients=["pperezm@fi.uba.ar"],
                body=f"""Nueva consulta desde El Portafolio:
                Nombre: {nombre} {apellido}
                Email: {email_usuario}
                Teléfono: {telefono}


MENSAJE: {mensaje}
                """)
            
            mail.send(msg_admin)

            # Mail para el usuario
            msg_usuario = Message(
                subject="Recibi tu mensaje - Pedro Perez Mochetti",
                recipients=[email_usuario],
                body=f"""Hola {nombre}, Gracias por contactarte!. Recibi tu mensaje y te respondere lo mas antes posible.
Tu mensaje: {mensaje}

Saludos,

Pedro Perez Mochetti
                """
            )

            mail.send(msg_usuario)
            return render_template(
                'contacto.html',
                titulo="Formulario Enviado Correctamente")

        except Exception: return jsonify({"error":"no se pudo enviar el mail"}),500
        
    return render_template('contacto.html')
