import os

import markdown
from cs50 import SQL
from flask import Flask, render_template, request
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown_checklist.extension import ChecklistExtension

from utils.profile import *
from utils.project import *

app = Flask(__name__)

# db = SQL(os.getenv("DATABASE_URL"))
db = SQL("sqlite:///database.db")


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/profile")
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
    more_about_you = db.execute("SELECT * FROM about_you")
    social_medias = db.execute("SELECT name, badge FROM social_medias")
    skills = db.execute("SELECT * FROM skills")

    return render_template(
        "profile.html",
        more_about_you=more_about_you,
        social_medias=social_medias,
        skills=skills,
        themes=features_themes,
        colors=features_color,
    )


@app.post("/profile")
def profile_post():
    markdown_str = ""

    # Title/Name
    name = request.form.get("name")
    if name:
        markdown_str += "# " + name + "\n"

    # Social Medias
    user_info = request.form.getlist("social_media_input")

    markdown_str += display_socials(user_info)

    # Subtitle
    subtitle = request.form.get("subtitle")
    if subtitle:
        greet = request.form.get("greet")
        markdown_str += "## " + greet + "\n"
        markdown_str += subtitle + "\n\n"

    # Profile Views
    if request.form.get("gh_views_check") == "true":
        markdown_str += (
            "![Profile Views](" + request.form.get("profile_views_url") + ")\n\n"
        )

    # More About You Section
    prefix = request.form.getlist("about_you_prefix")
    info = request.form.getlist("about_you_input")

    # Inputs with links
    prefix_links = request.form.getlist("about_you_link_prefix")
    info_links = request.form.getlist("about_you_link_input")

    markdown_str += display_about_you(prefix, info, prefix_links, info_links)

    # Skills Section
    skills_name = request.form.getlist("skill_name")

    if len(skills_name):
        markdown_str += display_skills(skills_name, request.form)

    # Cool Features Section
    markdown_str += display_features_profile(request.form)

    return markdown_str


@app.get("/project")
def project_get():
    skills = db.execute("SELECT * FROM skills")

    return render_template("project.html", skills=skills)


@app.post("/project")
def project_post():

    # --- Enter Section ---

    # About project
    project_name = request.form.get("project_name")
    brief_description = request.form.get("brief_description")
    project_status = request.form.get("project_status")

    # Badges
    pr_welcome = request.form.get("pr_welcome")
    badges = request.form.getlist("badges")
    gh_username = request.form.get("github_username")
    gh_repository = request.form.get("github_repository")

    enter_section = display_enter_section(
        project_name,
        brief_description,
        project_status,
        pr_welcome,
        badges,
        gh_username,
        gh_repository,
    )

    # --- About ---
    long_description = request.form.get("long_description")

    about = display_about(long_description)

    # --- Features ---
    features = request.form.getlist("features-check")

    features_mk = display_features_project(features, request.form)

    # --- Installation ---
    install_block = request.form.get("language_install")
    install_steps = request.form.get("steps_install")

    install = display_install(install_block, install_steps)

    # --- Usage ---
    usage_block = request.form.get("language_usage")
    usage_steps = request.form.get("steps_usage")

    usage = display_usage(usage_block, usage_steps)

    # --- Contact ---
    user_name = request.form.get("user_name")
    gh_username = request.form.get("github_username_contact")
    email = request.form.get("email")
    linkedin = request.form.get("linkedin")

    contact = display_contact(user_name, gh_username, email, linkedin)

    # --- Tech Stack ---
    skills_name = request.form.getlist("skill_name")

    tech_stack = display_skills(skills_name, request.form)

    # --- All mardkown ---
    markdown = gather_project_sections(
        enter_section, about, features_mk, install, usage, contact, tech_stack
    )

    return markdown


@app.post("/preview")
def submit():
    # Transform markdown data in html
    markdown_data = request.form["data"]
    return markdown.markdown(
        markdown_data, extensions=[FencedCodeExtension(), ChecklistExtension()]
    )


@app.get("/links&help")
def linkshelp():
    return render_template("links&help.html")


# if __name__ in "__main__":
#     app.run(debug=True)
