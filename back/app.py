from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {"message": "API funcionando"}, 200

if __name__ == "__main__":
    app.run(port=5002, debug=True)