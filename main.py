from flask import Flask, render_template
import json # reading widget data
import socket # hostname
import widget

app = Flask(__name__)

hostname = socket.gethostname()

@app.route("/")
def hello_world():
    app_list = [] 
    with open('config.json', 'r') as file:
        data = json.load(file)
    for application in data:
        app_list.append(widget.Widget(application['name'],
                                      5,
                                      application['ip'],
                                      application['port']))
    return render_template('index.html',
                           hostname = hostname,
                           app_list = app_list,
                           )
