import os
from cs50 import SQL
from flask import Flask, render_template, request
import markdown
app = Flask(__name__)

# db = SQL(os.getenv("DATABASE_URL"))
db = SQL("sqlite:///database.db")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile', methods=["GET", "POST"])
def profile():
    if request.method == 'POST':
        markdown_str = ''

        # Title/Name
        name = request.form.get('name')
        if name != '':
            markdown_str += '# ' + name + '\n'

        # Social Medias
        username = request.form.getlist('social_media_input')
        name = request.form.getlist('social_media_name')
        link = db.execute('SELECT badge, link FROM social_medias')
        title = False

        for i in range(len(username)):
            if username[i] != '':
                link_badge = str(link[i]['badge']).replace('username', str(username[i]))
                link_badge = link_badge.replace(str(name[i]), str(username[i]))

                markdown_str += '<img src="' + link_badge + '" alt="'+ str(name[i]) + ' Badge" height="25">&nbsp;\n'

        markdown_str += '\n'

        # Subtitle
        subtitle = request.form.get('subtitle')
        if subtitle != '':
            greet = request.form.get('greet')
            markdown_str += '## '+ str(greet) + '\n'
            markdown_str += subtitle + '\n\n'
        
        # Profile Views
        if request.form.get('gh_views_check') == 'true':
            markdown_str += '![Profile Views](' + str(request.form.get('profile_views_url')) + ')\n\n'

        # More About You Section
        prefix = request.form.getlist('about_you_prefix')
        info = request.form.getlist('about_you_input')
        title = False

        for i in range(len(info)):
            if info[i] != '':
                emoji = prefix[i][:1]
                pre = emoji + '&nbsp;' + prefix[i][2:]
                if title == False:
                    markdown_str += '### About me\n'
                    markdown_str += pre + ' ' + info[i] + '\n'
                    title = True
                else:
                    markdown_str += '<br/>' + pre + ' ' + info[i] + '\n'
        
        # Inputs with link
        prefix = request.form.getlist('about_you_link_prefix')
        info = request.form.getlist('about_you_link_input')
        for i in range(len(info)):
            link = str(info[i])
            if link != '':
                emoji = prefix[i][:1]
                pre = emoji + '&nbsp;' + prefix[i][2:]
    
                if link.find('www') != -1:
                    pre_link = 'https://'
                else:
                    pre_link = 'mailto:'
                
                if title == False:
                    markdown_str += '## About me\n'
                    markdown_str += pre + ' [' + link + '](' + pre_link + link + ')\n'
                    title = True
                else:
                    markdown_str += '<br/>' + pre + ' [' + link + '](' + pre_link + link + ')\n'

        markdown_str += '\n'

        # Skills Section
        skill_name = request.form.getlist('skill_name')
        
        if len(skill_name) > 0:
            markdown_str += '## Tech Stack\n'
            for skill in skill_name:
                markdown_str += '<img src="' + request.form.get(skill) + '" alt="' + skill + ' Badge" height="25">&nbsp;\n'
            markdown_str += '\n'

        # Cool Features Section
        features = ''
        # Github Status
        if request.form.get('gh_status_check') == 'true':
            features += '<img height="180em" src="' + str(request.form.get('gh_status_url')) + '">\n'

        # Top Languages Card
        if request.form.get('gh_top_languages_check') == 'true':        
            features += '<img height="180em" src="' + str(request.form.get('top_languages_url')) + '">\n'

        # Streak Stats
        if request.form.get('gh_streak_stats_check') == 'true':
            features += '<img height="180em" src="' + str(request.form.get('streak_stats_url')) +  '">\n'

        if features != '':
            markdown_str += '## GitHub Analytics\n'
            markdown_str += '<div>\n' + features + '</div>'

        return markdown_str
    
    # Get Method

    features_themes = [
        'dracula', 'dark', 'radical', 'merko', 'gruvbox', 'tokyonight', 'onedark', 'cobalt', 'synthwave', 'highcontrast' 
    ]

    features_color = [
        'brightgreen', 'green', 'yellow', 'yellowgreen', 'orange', 'red', 'grey', 'lightgrey', 'blueviolet'
    ]

    # Get information from database
    more_about_you = db.execute("SELECT * FROM about_you")
    social_medias = db.execute("SELECT * FROM social_medias")
    skills = db.execute("SELECT * FROM skills")

    return render_template('profile.html', more_about_you=more_about_you, social_medias=social_medias, skills=skills, themes=features_themes, colors=features_color)


@app.route('/project')
def project():
    return render_template('project.html')


@app.route('/preview', methods=['POST'])
def submit():
    # Transform markdown data in html 
    markdown_data = request.form['data']
    return markdown.markdown(markdown_data)


@app.route('/links&help')
def linkshelp():
    return render_template('links&help.html')
