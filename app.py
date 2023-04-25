#!/bin/env python3
''' minimal flask app for serving a plugin '''
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/plugins.xml")
def func1():
    ''' minimal flask app for serving a plugin '''
    return render_template('plugins.xml', static_url_path=app.static_url_path, root_url=request.root_url) 

@app.route("/")
def func2():
    ''' minimal flask app for serving a plugin '''
    return render_template('hello_world.html', agif=url_for('static',filename='RickAstley.gif'), root_url=request.root_url)

@app.route("/test")
def func3():
    ''' minimal flask app for serving a plugin '''
    return "<p>Hello, World!</p><p><img src=url_for('static', filename='RickAstley.gif') /></p>"

