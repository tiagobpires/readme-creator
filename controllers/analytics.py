from flask import Blueprint
from factory import db
from models import Analytics
from datetime import datetime
from sqlalchemy import func


analytics_controller = Blueprint(
    "analytics_controller", __name__, url_prefix="/analytics"
)


def get_current_day():
    today = datetime.utcnow()
    return today.strftime("%Y-%m-%d")


def get_analytics():
    analytics = Analytics.query.with_entities(
        func.sum(Analytics.profile_readme), func.sum(Analytics.project_readme)
    ).first()

    return {"profile": analytics[0], "project": analytics[1]}


@analytics_controller.get("/visits")
def count_visits():
    day = get_current_day()
    day = datetime.strptime(day, "%Y-%m-%d")

    current_day = Analytics.query.filter_by(date=day).first()

    if current_day:
        current_day.visits += 1
    else:
        current_day = Analytics(visits=1, date=day)
        db.session.add(current_day)

    db.session.commit()
    return {}, 200


@analytics_controller.get("/profile")
def count_profile_readmes():
    day = get_current_day()
    day = datetime.strptime(day, "%Y-%m-%d")

    current_day = Analytics.query.filter_by(date=day).first()
    current_day.profile_readme += 1

    db.session.commit()
    return {}, 200


@analytics_controller.get("/project")
def count_project_readmes():
    day = get_current_day()
    day = datetime.strptime(day, "%Y-%m-%d")

    current_day = Analytics.query.filter_by(date=day).first()

    current_day.project_readme += 1

    db.session.commit()
    return {}, 200
