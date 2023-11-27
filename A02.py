from flask import Flask, render_template

# Importa o módulo 'test'
import test

# Cria uma instância da classe Flask
app = Flask(__name__)

# Rota para a página inicial


@app.route("/")
def homepage():
    # Retorna uma mensagem HTML formatada quando a rota "/" é acessada
    return "<H1>Hello Web.py</H1>"

# Rota para "/start"


@app.route("/start")
def start():
    # Retorna a mensagem "Starting..." quando a rota "/start" é acessada
    return "Starting..."

# Rota para "/teste"


@app.route("/teste")
def lista_usuarios():
    # Renderiza um template chamado "teste.html" presente no diretório 'templates'
    return render_template("teste.html")


# Executa a aplicação Flask em modo de depuração
app.run(debug=True)
