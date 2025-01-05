from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Bianca Vieira v1.1"