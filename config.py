import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    APP_TITLE = "Readme Creator"

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "temp.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    uri = os.getenv("DATABASE_URL")
  
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://")

    @staticmethod
    def init_app(app):
        pass
