def display_enter_section(
    project_name,
    brief_description,
    project_status,
    pr_welcome,
    badges,
    gh_username,
    gh_repository,
):
    markdown = ""

    if project_name:
        markdown += f'<h1 align="center">\n\t{project_name}\n</h1>\n\n'

    if brief_description:
        markdown += f'<h3 align="center">\n\t{brief_description}\n</h3>\n\n'

    badges_images_tag = ""
    if pr_welcome:
        badges_images_tag += '<img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square"/>\n'

    for badge in badges:
        badges_images_tag += f'\t<img src="https://img.shields.io/github/{badge}/{gh_username}/{gh_repository}?color=green"/>\n'

    if badges_images_tag:
        markdown += f'<p align="center">\n\t{badges_images_tag}</p>\n\n'

    if project_status != "Open select menu":
        markdown += f'<h4 align="center">\n\tStatus: {project_status}\n</h4>\n\n'

    return markdown


def display_about(long_description):
    # Add new section if input was filled
    return f"## About\n{long_description}\n\n" if long_description else ""


def display_features_project(features_checked, form):
    markdown = ""

    # First input
    if form.get("feature1"):
        markdown = "## Features\n"

        # List with id of all features inserted
        list_features = form.get("list_features").split(",")

        for id in list_features:
            # Feature input
            feature = form.get(f"feature{id}")

            if f"feature{id}" in features_checked:
                markdown += f"* [x] {feature}\n"
            else:
                markdown += f"* [ ] {feature}\n"
        markdown += "\n"

    return markdown


def display_install(install_block, install_steps):
    markdown = ""

    if install_steps:
        markdown += (
            "## Installation\nTo Install this project, follow the steps above:\n"
        )
        markdown += f"```{install_block}\n{install_steps}\n```\n\n"

    return markdown


def display_usage(usage_block, usage_steps):
    markdown = ""

    if usage_steps:
        markdown += "## Usage\nTo use this project, follow the steps above:\n"
        markdown += f"```{usage_block}\n{usage_steps}\n```\n\n"

    return markdown


def display_contact(user_name, gh_username, email, linkedin):
    markdown = ""
    if user_name:
        markdown += f'<img align="left" src="https://avatars.githubusercontent.com/{gh_username}?size=100">\n\n'
        markdown += f"Made with ❤️ by [{user_name}](https://github.com/{gh_username}), enter in contact!\n\n"

    if email:
        markdown += f'<a href="mailto:{email}" target="_blank">'
        markdown += f'<img src="https://img.shields.io/badge/{email}-D14836?style=flat&logo=gmail&logoColor=white" alt="Email Badge" height="25"></a>&nbsp;\n'

    if linkedin:
        markdown += f'<a href="https://www.linkedin.com/in/{linkedin}" target="_blank">'
        markdown += f'<img src="https://img.shields.io/badge/{linkedin}-0077B5?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn Badge" height="25"></a>&nbsp;\n'

    if markdown:
        markdown = f'## Contact\n{markdown}\n<br clear="left"/>\n'

    return markdown


def display_skills(skills_name, form):
    markdown = ""

    for skill in skills_name:
        markdown += (
            '<img src="'
            + form.get(skill)
            + '" alt="'
            + skill
            + ' Badge" height="25">&nbsp;\n'
        )

    # Add new section if input was filled
    return f"## Tech Stack\n{markdown}\n" if markdown else ""


def gather_project_sections(
    enter_section, about, features_mk, install, usage, contact, tech_stack
):

    index = '<p align="center">\n'

    if about:
        index += '\t<a href="#about">About</a> •\n'

    if features_mk:
        index += '\t<a href="#features">Features</a> •\n'

    if tech_stack:
        index += '\t<a href="#tech-stack">Tech Stack</a> •\n'

    if install:
        index += '\t<a href="#installation">Installation</a> •\n'

    if usage:
        index += '\t<a href="#usage">Usage</a> • \n'

    if contact:
        index += '\t<a href="#contact">Contact</a> •\n'

    # Remove last character (•)
    index = index[:-2]

    index += "\n</p>\n\n"

    return f"{enter_section}{index}{about}{features_mk}{tech_stack}{install}{usage}{contact}"
