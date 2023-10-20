from flask import Blueprint, render_template

rotas = Blueprint('rotas', __name__)

@rotas.route('/')
def home():
    return render_template('home.html')


@rotas.route('/painel')
def index():
    return render_template('index.html')
