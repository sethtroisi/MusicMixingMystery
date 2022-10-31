"""
Main app for MusicMixingMystery

Can run with
$ FLASK_APP=main.py FLASK_ENV=development flask run
or
$ python main.py
"""

import os

from flask import Flask, render_template

from app import create_app
from routes.hello_world import Welcome

api, app = create_app()

# For routing rest requests
#api.add_resource(Welcome, "/", "/hello")

@app.route('/')
@app.route('/hello/')
def hello():
    return render_template("home_page.html")

@app.route('/quiz')
def quiz():
    return render_template("quiz.html")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
