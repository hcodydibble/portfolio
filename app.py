from flask import Flask, render_template, send_from_directory
import os
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

@app.route('/knightdefense')
def game_view():
    return render_template('game.html')


@app.route('/codydibble')
def download_resume():
    directory = os.path.join(app.static_folder, 'files/')
    return send_from_directory(directory=directory, filename='codydibble.docx')
