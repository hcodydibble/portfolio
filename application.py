from flask import Flask, render_template, url_for, request
app = Flask(__name__)


@app.route('/')
def home_view():
    return render_template('home.html')


@app.route('/about')
def about_view():
    return render_template('about.html')


@app.route('/projects')
def projects_view():
    return render_template('projects.html')


@app.route('/contact')
def contact_view():
    return render_template('contact.html')
