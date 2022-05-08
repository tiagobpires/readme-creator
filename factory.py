from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    from models import AboutYou, Analytics, Skill, SocialMedia

    migrate.init_app(app, db)

    @app.get("/")
    def index():
        from controllers.analytics import get_analytics

        analytics = get_analytics()

        profile = analytics["profile"]
        project = analytics["project"]

        return render_template("index.html", profile=profile, project=project)

    @app.get("/links&help")
    def links_help():
        return render_template("links&help.html")

    from controllers import analytics_controller, readme_controller

    app.register_blueprint(analytics_controller)
    app.register_blueprint(readme_controller)

    return app
