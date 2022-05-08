import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    APP_TITLE = "Readme Creator"

    uri = os.getenv("DATABASE_URL")

    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = uri

    @staticmethod
    def init_app(app):
        pass
