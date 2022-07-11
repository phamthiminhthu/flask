from flask import render_template, request, redirect, url_for
from flask_blog import app

@app.route('/')
def show_entries():
    return render_template('entries/index.html')

