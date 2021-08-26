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

    social_medias = {
        '@gmail.com' : 'https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white',
        'dev to' : 'https://img.shields.io/badge/dev.to-0A0A0A?style=for-the-badge&logo=dev.to&logoColor=white',
        'github username' : 'https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white', 
        'tiktok' : 'https://img.shields.io/badge/TikTok-000000?style=for-the-badge&logo=tiktok&logoColor=white',
        'twich channel' : 'https://img.shields.io/badge/Twitch-9146FF?style=for-the-badge&logo=twitch&logoColor=white',
        'medium' : 'https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white',
        'linkedin profile' : 'https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white',
        'twitter' : 'https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white',
        'instagram username' : 'https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white',
        'youtube channel' : 'https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white'
    }

    skills = {
        'android' : 'https://github.com/devicons/devicon/raw/master/icons/android/android-plain-wordmark.svg',
        'angular' : 'https://github.com/devicons/devicon/raw/master/icons/angularjs/angularjs-plain-wordmark.svg',
        'apache' : 'https://github.com/devicons/devicon/raw/master/icons/apache/apache-plain-wordmark.svg',
        'arduino' : 'https://github.com/devicons/devicon/raw/master/icons/arduino/arduino-original-wordmark.svg',
        'bash' : 'https://github.com/devicons/devicon/raw/master/icons/bash/bash-original.svg',
        'bootstrap' : 'https://github.com/devicons/devicon/raw/master/icons/bootstrap/bootstrap-plain-wordmark.svg',
        'c' : 'https://github.com/devicons/devicon/raw/master/icons/c/c-original.svg',
        'canva' : 'https://github.com/devicons/devicon/raw/master/icons/canva/canva-original.svg',
        'c++' : 'https://github.com/devicons/devicon/raw/master/icons/cplusplus/cplusplus-original.svg',
        'csharp' : 'https://github.com/devicons/devicon/raw/master/icons/csharp/csharp-original.svg',
        'css3' : 'https://github.com/devicons/devicon/raw/master/icons/css3/css3-plain-wordmark.svg',
        'dart' : 'https://github.com/devicons/devicon/raw/master/icons/dart/dart-plain-wordmark.svg',
        'django' : 'https://github.com/devicons/devicon/raw/master/icons/django/django-line.svg',
        'docker' : 'https://github.com/devicons/devicon/raw/master/icons/docker/docker-original-wordmark.svg',
        'elixir' : 'https://github.com/devicons/devicon/raw/master/icons/elixir/elixir-original-wordmark.svg',
        'figma' : 'https://github.com/devicons/devicon/raw/master/icons/figma/figma-original.svg',
        'flask' : 'https://github.com/devicons/devicon/raw/master/icons/flask/flask-original-wordmark.svg',
        'firebase' : 'https://github.com/devicons/devicon/raw/master/icons/firebase/firebase-plain-wordmark.svg',
        'flutter' : 'https://github.com/devicons/devicon/raw/master/icons/flutter/flutter-original.svg',
        'git' : 'https://github.com/devicons/devicon/raw/master/icons/git/git-plain-wordmark.svg',
        'go' : 'https://github.com/devicons/devicon/raw/master/icons/go/go-original.svg',
        'html5' : 'https://github.com/devicons/devicon/raw/master/icons/html5/html5-plain-wordmark.svg',
        'haskell' : 'https://github.com/devicons/devicon/raw/master/icons/haskell/haskell-original-wordmark.svg',
        'illustrator' : 'https://github.com/devicons/devicon/raw/master/icons/illustrator/illustrator-plain.svg',
        'ionic' : 'https://github.com/devicons/devicon/raw/master/icons/ionic/ionic-original-wordmark.svg',
        'java' : 'https://github.com/devicons/devicon/raw/master/icons/java/java-original-wordmark.svg',
        'javascript' : 'https://github.com/devicons/devicon/raw/master/icons/javascript/javascript-original.svg',
        'jQuery' : 'https://github.com/devicons/devicon/raw/master/icons/jquery/jquery-plain-wordmark.svg',
        'kotlin' : 'https://github.com/devicons/devicon/raw/master/icons/kotlin/kotlin-plain-wordmark.svg',
        'laravel' : 'https://github.com/devicons/devicon/raw/master/icons/laravel/laravel-plain.svg',
        'lua' : 'https://github.com/devicons/devicon/raw/master/icons/lua/lua-original-wordmark.svg',
        'matlab' : 'https://github.com/devicons/devicon/raw/master/icons/matlab/matlab-original.svg',
        'myql' : 'https://github.com/devicons/devicon/raw/master/icons/mysql/mysql-original-wordmark.svg',
        'nodejs' : 'https://github.com/devicons/devicon/raw/master/icons/nodejs/nodejs-plain-wordmark.svg',
        'numpy' : 'https://github.com/devicons/devicon/raw/master/icons/numpy/numpy-original-wordmark.svg',
        'oracle' : 'https://github.com/devicons/devicon/raw/master/icons/oracle/oracle-original.svg',
        'opengl' : 'https://github.com/devicons/devicon/raw/master/icons/opengl/opengl-plain.svg',
        'photoshop' : 'https://github.com/devicons/devicon/raw/master/icons/photoshop/photoshop-line.svg',
        'php' : 'https://github.com/devicons/devicon/raw/master/icons/php/php-original.svg',
        'postgreesql' : 'https://github.com/devicons/devicon/raw/master/icons/postgresql/postgresql-plain-wordmark.svg',
        'python' : 'https://github.com/devicons/devicon/raw/master/icons/python/python-original-wordmark.svg',
        'r' : 'https://github.com/devicons/devicon/raw/master/icons/r/r-original.svg',
        'react' : 'https://github.com/devicons/devicon/raw/master/icons/react/react-original-wordmark.svg',
        'swift' : 'https://github.com/devicons/devicon/raw/master/icons/swift/swift-original.svg',
        'typescript' : 'https://github.com/devicons/devicon/raw/master/icons/typescript/typescript-original.svg',
        'unity' : 'https://github.com/devicons/devicon/raw/master/icons/unity/unity-original-wordmark.svg', 
        'vuejs' : 'https://github.com/devicons/devicon/raw/master/icons/vuejs/vuejs-original-wordmark.svg'
    }


    just_original = {
        'android' : 'https://github.com/devicons/devicon/raw/master/icons/android/android-original.svg',
        'angular' : 'https://github.com/devicons/devicon/raw/master/icons/angularjs/angularjs-original.svg',
        'apache' : 'https://github.com/devicons/devicon/raw/master/icons/apache/apache-original.svg',
        'arduino' : 'https://github.com/devicons/devicon/raw/master/icons/arduino/arduino-original.svg',
        'bash' : 'https://github.com/devicons/devicon/raw/master/icons/bash/bash-original.svg',
        'bootstrap' : 'https://github.com/devicons/devicon/raw/master/icons/bootstrap/bootstrap-original.svg',
        'c' : 'https://github.com/devicons/devicon/raw/master/icons/c/c-original.svg',
        'canva' : 'https://github.com/devicons/devicon/raw/master/icons/canva/canva-original.svg',
        'c++' : 'https://github.com/devicons/devicon/raw/master/icons/cplusplus/cplusplus-original.svg',
        'csharp' : 'https://github.com/devicons/devicon/raw/master/icons/csharp/csharp-original.svg',
        'css3' : 'https://github.com/devicons/devicon/raw/master/icons/css3/css3-original.svg',
        'dart' : 'https://github.com/devicons/devicon/raw/master/icons/dart/dart-original.svg',
        'django' : 'https://github.com/devicons/devicon/raw/master/icons/django/django-line.svg',
        'docker' : 'https://github.com/devicons/devicon/raw/master/icons/docker/docker-original-wordmark.svg',
        'elixir' : 'https://github.com/devicons/devicon/raw/master/icons/elixir/elixir-original.svg',
        'figma' : 'https://github.com/devicons/devicon/raw/master/icons/figma/figma-original.svg',
        'flask' : 'https://github.com/devicons/devicon/raw/master/icons/flask/flask-original.svg',
        'firebase' : 'https://github.com/devicons/devicon/raw/master/icons/firebase/firebase-plain.svg',
        'flutter' : 'https://github.com/devicons/devicon/raw/master/icons/flutter/flutter-original.svg',
        'git' : 'https://github.com/devicons/devicon/raw/master/icons/git/git-original.svg',
        'go' : 'https://github.com/devicons/devicon/raw/master/icons/go/go-original.svg',
        'html5' : 'https://github.com/devicons/devicon/raw/master/icons/html5/html5-original.svg',
        'haskell' : 'https://github.com/devicons/devicon/raw/master/icons/haskell/haskell-original.svg',
        'illustrator' : 'https://github.com/devicons/devicon/raw/master/icons/illustrator/illustrator-plain.svg',
        'ionic' : 'https://github.com/devicons/devicon/raw/master/icons/ionic/ionic-original.svg',
        'java' : 'https://github.com/devicons/devicon/raw/master/icons/java/java-original.svg',
        'javascript' : 'https://github.com/devicons/devicon/raw/master/icons/javascript/javascript-original.svg',
        'jQuery' : 'https://github.com/devicons/devicon/raw/master/icons/jquery/jquery-original.svg',
        'kotlin' : 'https://github.com/devicons/devicon/raw/master/icons/kotlin/kotlin-original.svg',
        'laravel' : 'https://github.com/devicons/devicon/raw/master/icons/laravel/laravel-plain.svg',
        'lua' : 'https://github.com/devicons/devicon/raw/master/icons/lua/lua-original.svg',
        'matlab' : 'https://github.com/devicons/devicon/raw/master/icons/matlab/matlab-original.svg',
        'mysql' : 'https://github.com/devicons/devicon/raw/master/icons/mysql/mysql-original.svg',
        'nodejs' : 'https://github.com/devicons/devicon/raw/master/icons/nodejs/nodejs-original.svg',
        'numpy' : 'https://github.com/devicons/devicon/raw/master/icons/numpy/numpy-original.svg',
        'oracle' : 'https://github.com/devicons/devicon/raw/master/icons/oracle/oracle-original.svg',
        'opengl' : 'https://github.com/devicons/devicon/raw/master/icons/opengl/opengl-plain.svg',
        'photoshop' : 'https://github.com/devicons/devicon/raw/master/icons/photoshop/photoshop-line.svg',
        'php' : 'https://github.com/devicons/devicon/raw/master/icons/php/php-original.svg',
        'postgresql' : 'https://github.com/devicons/devicon/raw/master/icons/postgresql/postgresql-original.svg',
        'python' : 'https://github.com/devicons/devicon/raw/master/icons/python/python-original.svg',
        'r' : 'https://github.com/devicons/devicon/raw/master/icons/r/r-original.svg',
        'react' : 'https://github.com/devicons/devicon/raw/master/icons/react/react-original.svg',
        'swift' : 'https://github.com/devicons/devicon/raw/master/icons/swift/swift-original.svg', 
        'typescript' : 'https://github.com/devicons/devicon/raw/master/icons/typescript/typescript-original.svg',
        'unity' : 'https://github.com/devicons/devicon/raw/master/icons/unity/unity-original.svg', 
        'vuejs' : 'https://github.com/devicons/devicon/raw/master/icons/vuejs/vuejs-original.svg'
    }

    return render_template('profile.html', more_about_you=more_about_you, social_medias=social_medias, skills=skills)
    