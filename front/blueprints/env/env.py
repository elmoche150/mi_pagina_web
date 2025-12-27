from flask import Flask,render_template
from flask_mail import Mail
from dotenv import load_dotenv
import os


"""Obtiene informacion del .env"""
load_dotenv()
mail = Mail()
"""información para hacer el envío de mails"""
def config_mail(app):
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == "True"
    app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL') == "True"
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
    mail.init_app(app)