import markdown
from flask import Blueprint, render_template, request
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown_checklist.extension import ChecklistExtension
from models import AboutYou, Skill, SocialMedia
from utils.profile import ProfileForm
from utils.project import ProjectForm


readme_controller = Blueprint("readme_controller", __name__)


@readme_controller.get("/profile")
def profile_get():
    features_themes = [
        "dracula",
        "dark",
        "radical",
        "merko",
        "gruvbox",
        "tokyonight",
        "onedark",
        "cobalt",
        "synthwave",
        "highcontrast",
    ]

    features_color = [
        "brightgreen",
        "green",
        "yellow",
        "yellowgreen",
        "orange",
        "red",
        "grey",
        "lightgrey",
        "blueviolet",
    ]

    # Get information from database
    more_about_you = AboutYou.query.all()
    social_medias = SocialMedia.query.filter_by(badge_type="with_username").all()
    skills = Skill.query.filter_by(badge_type="dark_with_name").all()

    return render_template(
        "profile.html",
        more_about_you=more_about_you,
        social_medias=social_medias,
        skills=skills,
        themes=features_themes,
        colors=features_color,
    )


@readme_controller.post("/profile")
def profile_post():
    profile_form = ProfileForm(request.form)

    return profile_form.create_markdown()


@readme_controller.get("/project")
def project_get():
    skills = Skill.query.filter_by(badge_type="dark_with_name").all()

    return render_template("project.html", skills=skills)


@readme_controller.post("/project")
def project_post():
    project_form = ProjectForm(request.form)

    return project_form.create_markdown()


@readme_controller.post("/preview")
def submit():
    # Transform markdown data in html
    markdown_data = request.form["data"]
    return markdown.markdown(
        markdown_data, extensions=[FencedCodeExtension(), ChecklistExtension()]
    )
