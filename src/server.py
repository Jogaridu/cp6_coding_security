from flask import Flask

from routes.rotas import rotas
from controllers.home import home

app = Flask(__name__, static_folder='static')
app.secret_key = 'packetguardian'

app.config['DEBUG'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.register_blueprint(rotas)
app.register_blueprint(home)

if __name__ == '__main__': 
    app.run()
