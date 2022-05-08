from factory import db


class AboutYou(db.Model):
    __tablename__ = "about_you"

    id = db.Column(db.Integer, primary_key=True)
    prefix = db.Column(db.Text, nullable=False)
    place_holder = db.Column(db.Text, nullable=False)


class Skill(db.Model):
    __tablename__ = "skills"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    badge_link = db.Column(db.Text, nullable=False)
    badge_type = db.Column(db.String(20), nullable=False, index=True)


class SocialMedia(db.Model):
    __tablename__ = "social_medias"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    social_link = db.Column(db.Text, nullable=False)
    badge_link = db.Column(db.Text, nullable=False)
    badge_type = db.Column(db.Text, nullable=False, index=True)


class Analytics(db.Model):
    __tablename__ = "analytics"

    id = db.Column(db.Integer, primary_key=True)
    visits = db.Column(db.Integer, default=0)
    profile_readme = db.Column(db.Integer, default=0)
    project_readme = db.Column(db.Integer, default=0)
    date = db.Column(db.DateTime, nullable=False, index=True)
