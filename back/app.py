from flask import Flask
import os

from routes.registrarse.registrarse import registrarse_bp

app = Flask(__name__)


app.register_blueprint(registrarse_bp, url_prefix="/registrarse")

@app.route('/')
def index():
    return {"message": "API funcionando"}, 200

if __name__ == "__main__":
    app.run(port=5002, debug=True)