from cs50 import SQL
from flask import Flask, render_template, request
import markdown
app = Flask(__name__)

db = SQL('sqlite:///database.db')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile', methods=["GET", "POST"])
def profile():
    if request.method == 'POST':
        markdown_str = ''

        # Greet Section
        name = request.form.get('name')
        if name != '':
            title = request.form.get('title')
            markdown_str += '# ' + title + ' ' + name + '\n\n'

        subtitle = request.form.get('subtitle')
        if subtitle != '':
            markdown_str += '### ' + subtitle + '\n\n'

        # More About You Section
        prefix = request.form.getlist('more_about_you_prefix')
        info = request.form.getlist('more_about_you_input')
        title = False

        for i in range(len(info)):
            if info[i] != '':
                if title == False:
                    markdown_str += '## About me\n'
                    title = True

                markdown_str += prefix[i] + ' ' + info[i] + '\n\n'

        # Social Medias Section
        username = request.form.getlist('social_media_input')
        name = request.form.getlist('social_media_name')
        link = db.execute('SELECT badge, link FROM social_medias')
        title = False

        for i in range(len(username)):
            if username[i] != '':
                if title == False:
                    markdown_str += '## Contact me:\n'
                    title = True

                markdown_str += '[![' + str(name[i]).capitalize() + ' Badge]'
                markdown_str += '(' + str(link[i]['badge']) + ')]'
                markdown_str += '(' + str(link[i]['link']).replace('username', str(username[i])) + ')&nbsp;\n'
        if title == True:
            markdown_str += '\n'

        # Skills Section
        skill_name = request.form.getlist('skill_name')
        
        if len(skill_name) > 0:
            markdown_str += '## My Skills\n'
            for skill in skill_name:
                markdown_str += '<img src="' + request.form.get(skill) + '" alt="' + skill + ' Badge" height="50" width="50">&nbsp;\n'
            markdown_str += '\n'

        # Cool Features Section
        # Github Status
        if request.form.get('gh_status_check') == 'true':
            markdown_str += '![GitHub stats](' + str(request.form.get('gh_status_url')) + ')\n'

        # Top Languages Card
        if request.form.get('gh_top_languages_check') == 'true':        
            markdown_str += '![Top Languages](' + str(request.form.get('top_languages_url')) + ')\n'

        # Profile Views
        if request.form.get('gh_views_check') == 'true':
            markdown_str += '![Profile Views](' + str(request.form.get('profile_views_url')) + ')\n'

        # Streak Stats
        if request.form.get('gh_streak_stats_check') == 'true':
            markdown_str += '![Streak Stats](' + str(request.form.get('streak_stats_url')) + ')\n'

        return markdown_str
    
    # Get Method
    features_themes = [
        'dracula', 'dark', 'radical', 'merko', 'gruvbox', 'tokyonight', 'onedark', 'cobalt', 'synthwave', 'highcontrast' 
    ]

    features_color = [
        'brightgreen', 'green', 'yellow', 'yellowgreen', 'orange', 'red', 'grey', 'lightgrey', 'blueviolet'
    ]

    more_about_you = db.execute("SELECT * FROM about_you")
    
    social_medias = db.execute("SELECT * FROM social_medias")
    
    skills = db.execute('SELECT * FROM skills')

    return render_template('profile.html', more_about_you=more_about_you, social_medias=social_medias, skills=skills, themes=features_themes, colors=features_color)


@app.route('/preview', methods=['POST'])
def submit():
    markdown_data = request.form['data']
    return markdown.markdown(markdown_data)
