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

    more_about_you = db.execute("SELECT * FROM about_you")
    
    social_medias = db.execute("SELECT * FROM social_medias")
    
    skills = {'android': 'https://img.shields.io/badge/Android-05122A?style=flat&logo=android', 'angular': 'https://img.shields.io/badge/Angular-05122A?style=flat&logo=angular', 'apache': 'https://img.shields.io/badge/Apache-05122A?style=flat&logo=apache', 'arduino': 'https://img.shields.io/badge/Arduino-05122A?style=flat&logo=arduino', 'bash': 'https://img.shields.io/badge/Bash-05122A?style=flat&logo=bash', 'bootstrap': 'https://img.shields.io/badge/Bootstrap-05122A?style=flat&logo=bootstrap', 'c': 'https://img.shields.io/badge/C-05122A?style=flat&logo=c', 'canva': 'https://img.shields.io/badge/Canva-05122A?style=flat&logo=canva', 'c++': 'https://img.shields.io/badge/C++-05122A?style=flat&logo=c%2B%2B&', 'csharp': 'https://img.shields.io/badge/Csharp-05122A?style=flat&logo=csharp', 'css3': 'https://img.shields.io/badge/Css3-05122A?style=flat&logo=css3', 'dart': 'https://img.shields.io/badge/Dart-05122A?style=flat&logo=dart', 'django': 'https://img.shields.io/badge/Django-05122A?style=flat&logo=django', 'docker': 'https://img.shields.io/badge/Docker-05122A?style=flat&logo=docker', 'elixir': 'https://img.shields.io/badge/Elixir-05122A?style=flat&logo=elixir', 'figma': 'https://img.shields.io/badge/Figma-05122A?style=flat&logo=figma', 'flask': 'https://img.shields.io/badge/Flask-05122A?style=flat&logo=flask', 'firebase': 'https://img.shields.io/badge/Firebase-05122A?style=flat&logo=firebase', 'flutter': 'https://img.shields.io/badge/Flutter-05122A?style=flat&logo=flutter', 'git': 'https://img.shields.io/badge/Git-05122A?style=flat&logo=git', 'go': 'https://img.shields.io/badge/Go-05122A?style=flat&logo=go', 'html5': 'https://img.shields.io/badge/Html5-05122A?style=flat&logo=html5', 'haskell': 'https://img.shields.io/badge/Haskell-05122A?style=flat&logo=haskell', 'illustrator': 'https://img.shields.io/badge/Illustrator-05122A?style=flat&logo=adobeillustrator', 'ionic': 'https://img.shields.io/badge/Ionic-05122A?style=flat&logo=ionic', 'java': 'https://img.shields.io/badge/Java-05122A?style=flat&logo=java', 'javascript': 'https://img.shields.io/badge/Javascript-05122A?style=flat&logo=javascript', 'jQuery': 'https://img.shields.io/badge/Jquery-05122A?style=flat&logo=jQuery', 'kotlin': 'https://img.shields.io/badge/Kotlin-05122A?style=flat&logo=kotlin', 'laravel': 'https://img.shields.io/badge/Laravel-05122A?style=flat&logo=laravel', 'lua': 'https://img.shields.io/badge/Lua-05122A?style=flat&logo=lua', 'matlab': 'https://img.shields.io/badge/Matlab-05122A?style=flat&logo=matlab', 'mysql': 'https://img.shields.io/badge/Mysql-05122A?style=flat&logo=mysql', 'nodejs': 'https://img.shields.io/badge/Nodejs-05122A?style=flat&logo=node.js', 'numpy': 'https://img.shields.io/badge/Numpy-05122A?style=flat&logo=numpy', 'oracle': 'https://img.shields.io/badge/Oracle-05122A?style=flat&logo=oracle', 'opengl': 'https://img.shields.io/badge/Opengl-05122A?style=flat&logo=opengl', 'photoshop': 'https://img.shields.io/badge/Photoshop-05122A?style=flat&logo=adobephotoshop', 'php': 'https://img.shields.io/badge/Php-05122A?style=flat&logo=php', 'postgresql': 'https://img.shields.io/badge/Postgresql-05122A?style=flat&logo=postgresql', 'python': 'https://img.shields.io/badge/Python-05122A?style=flat&logo=python', 'r': 'https://img.shields.io/badge/R-05122A?style=flat&logo=r', 'react': 'https://img.shields.io/badge/React-05122A?style=flat&logo=react', 'swift': 'https://img.shields.io/badge/Swift-05122A?style=flat&logo=swift', 'typescript': 'https://img.shields.io/badge/Typescript-05122A?style=flat&logo=typescript', 'unity': 'https://img.shields.io/badge/Unity-05122A?style=flat&logo=unity', 'vuejs': 'https://img.shields.io/badge/Vuejs-05122A?style=flat&logo=vuedotjs'}

    return render_template('profile.html', more_about_you=more_about_you, social_medias=social_medias, skills=skills, themes=features_themes, colors=features_color)


@app.route('/project')
def project():
    return render_template('project.html')


@app.route('/preview', methods=['POST'])
def submit():
    markdown_data = request.form['data']
    return markdown.markdown(markdown_data)


@app.route('/links&help')
def goahead():
    return render_template('links&help.html')
