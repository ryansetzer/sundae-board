from flask import Flask, render_template
import json # reading widget data
import os # defining path
import socket # hostname

app = Flask(__name__)

hostname = socket.gethostname()

@app.route("/")
def hello_world():
    app_list = []
    file = open('config.json')
    data = json.load(file)
    for application in data:
        app_list.append(application)
    return render_template("index.html",
                           hostname = hostname,
                           app_list = app_list,
                           )
