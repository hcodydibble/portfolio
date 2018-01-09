from flask import Flask, render_template, url_for, request
app = Flask(__name__)


@app.route('/')
def home_view():
    return render_template('home.html')
