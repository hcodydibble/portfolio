from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def home_view():
    url_for('static', filename='style.css')
    return render_template('home.html')
