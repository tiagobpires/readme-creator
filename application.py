from cs50 import SQL
from flask import Flask, json, render_template, request, jsonify

app = Flask(__name__)

db = SQL('sqlite:///database.db')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
def profile():

    more_about_you = db.execute("SELECT * FROM about_you")
    
    social_medias = db.execute("SELECT * FROM social_medias")
    
    skills = db.execute('SELECT * FROM skills')

    return render_template('profile.html', more_about_you=more_about_you, social_medias=social_medias, skills=skills)


@app.route('/submit', methods=['POST'])
def submit():
    markdown = ''
    name = request.form.get('name')
    if name != '':
        title = request.form.get('title')
        markdown += '# ' + title + ' ' + name + '\n'

    subtitle = request.form.get('subtitle')
    if subtitle != '':
        markdown += '### ' + subtitle + '\n'

    more_about_you_keys = request.form.getlist('more_about_you_key')
    more_about_you_values = request.form.getlist('more_about_you_value')
    more_about_you = {}
    for i in range(0, len(more_about_you_values)):
        if more_about_you_values[i] != '':
            more_about_you[more_about_you_keys[i]] = more_about_you_values[i]
    
    if len(more_about_you) != 0:
        markdown += '## About me\n'
        for key, value in more_about_you.items():
            markdown += key + ' ' + value + '\n\n'


    print(markdown)
    return markdown


@app.route('/teste')
def teste():
    return render_template('teste.html')