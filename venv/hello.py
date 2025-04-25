from flask import Flask #importando o Flask

app = Flask(__name__)

@app.route("/") #rota que vamos utilizar
def hello_world():
    return "<p>Hello, Wolrd!</p>"