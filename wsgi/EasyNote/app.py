#-*- coding: utf-8 -*-

from flask import Flask,redirect
from master.app import master

SECRET_KEY = '0xABC'

app = Flask(__name__, static_folder='master/static')
app.config.from_object(__name__)
app.register_blueprint(master)

if __name__ == '__main__':
    app.run(debug=True)
