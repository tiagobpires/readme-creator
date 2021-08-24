from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
def profile():

    more_about_you = {
        '🔭 I’m currently working on' : 'Be a good student :P',
        '🎓 Graduated in ' : '',
        '📫 Reach me ' : 'tiagobarrospires@gmail.com',
        "💡 I'm interested about " : 'Computer Science, web development, games and series',
        '👨‍💻 See my portfolio at ' : 'www.portfolio.com',
        '💬 Ask me about ' : 'Competitive programming',
        '🌱 Learning about ' : 'Web development and Competitive programming',
        '🤝 I like to collaborate in ' : 'Open Source projects',
        '😄 Pronouns ' : 'He/His',
        '⚡ Fun fact ' : ':0'
    }

    return render_template('profile.html', more_about_you=more_about_you)
    