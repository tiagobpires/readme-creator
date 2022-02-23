import os

import markdown
from cs50 import SQL
from flask import Flask, render_template, request

from helpers import *

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
            "![Profile Views](" + str(request.form.get("profile_views_url")) + ")\n\n"
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
    markdown_str += display_features(request.form)

    return markdown_str


@app.get("/project")
def project():
    return render_template("project.html")


@app.post("/preview")
def submit():
    # Transform markdown data in html
    markdown_data = request.form["data"]
    return markdown.markdown(markdown_data)


@app.get("/links&help")
def linkshelp():
    return render_template("links&help.html")


if __name__ in "__main__":
    app.run(debug=True)
