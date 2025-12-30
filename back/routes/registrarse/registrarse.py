from flask import Blueprint, jsonify, request
from routes.db.db import get_connection

registrarse_bp = Blueprint("registrarse", __name__)

@registrarse_bp.route('/registrar', methods=['POST'])
def registrar_usuario():

    data = request.get_json()
    nombre= data.get('nombre')
    email= data.get('email')
    contraseña= data.get('contrasena')

    conn = get_connection()
    cursor = conn.cursor(dictionary=True) 
    
    cursor.execute("SELECT * FROM datos_del_usuario WHERE email_del_usuario = %s ", (email,))
    existe_mail = cursor.fetchone()

    if existe_mail:
        cursor.close()
        conn.close()
        return jsonify({"error": "EL EMAIL YA EXISTE"}), 400
    
    cursor.execute("""
    INSERT INTO datos_del_usuario (nombre_del_usuario, email_del_usuario, contraseña_del_usuario)
    VALUES (%s, %s, %s) """, (nombre, email, contraseña))

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Usuario registrado con éxito"}, 201




