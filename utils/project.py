class ProjectForm:
    def __init__(self, form):
        self.form = form
        self.markdown = ""
        self.about = ""
        self.features = ""
        self.install = ""
        self.usage = ""
        self.contact = ""
        self.skills = ""
        self.index = ""

    def create_markdown(self):
        self.add_enter_section()

        self.add_about()
        self.add_features()
        self.add_install()
        self.add_usage()
        self.add_contact()
        self.add_skills()
        self.add_index()

        self.markdown += f"{self.index}{self.about}{self.features}{self.skills}{self.install}{self.usage}{self.contact}"

        return self.markdown

    def add_enter_section(self):
        # About project
        project_name = self.form.get("project_name")
        if project_name:
            self.markdown += f'<h1 align="center">\n\t{project_name}\n</h1>\n\n'

        brief_description = self.form.get("brief_description")
        if brief_description:
            self.markdown += f'<h3 align="center">\n\t{brief_description}\n</h3>\n\n'

        # Badges
        pr_welcome = self.form.get("pr_welcome")
        badges = self.form.getlist("badges")
        gh_username = self.form.get("github_username")
        gh_repository = self.form.get("github_repository")
        badges_tag = ""

        if pr_welcome:
            badges_tag += '\t<img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square"/>\n'

        for badge in badges:
            badges_tag += f'\t<img src="https://img.shields.io/github/{badge}/{gh_username}/{gh_repository}?color=green"/>\n'

        if badges_tag:
            self.markdown += f'<p align="center">\n{badges_tag}</p>\n\n'

        # Project status
        project_status = self.form.get("project_status")

        if project_status != "Open select menu":
            self.markdown += (
                f'<h4 align="center">\n\tStatus: {project_status}\n</h4>\n\n'
            )

    def add_about(self):
        long_description = self.form.get("long_description")

        if long_description:
            self.about = f"## About\n{long_description}\n\n"

    def add_features(self):
        self.features = ""

        # First input
        if self.form.get("feature1"):
            self.features += "## Features\n"

            # List with id of all features inserted
            list_features = self.form.get("list_features").split(",")

            features_checked = self.form.getlist("features-check")

            for id in list_features:
                # Feature input
                feature = self.form.get(f"feature{id}")

                if f"feature{id}" in features_checked:
                    self.features += f"* [x] {feature}\n"
                else:
                    self.features += f"* [ ] {feature}\n"
            self.features += "\n"

    def add_install(self):
        install_block = self.form.get("language_install")
        install_steps = self.form.get("steps_install")

        if install_steps:
            self.install += (
                "## Installation\nTo Install this project, follow the steps above:\n"
            )
            self.install += f"```{install_block}\n{install_steps}\n```\n\n"

    def add_usage(self):
        usage_block = self.form.get("language_usage")
        usage_steps = self.form.get("steps_usage")

        if usage_steps:
            self.usage += "## Usage\nTo use this project, follow the steps above:\n"
            self.usage += f"```{usage_block}\n{usage_steps}\n```\n\n"

    def add_contact(self):
        user_name = self.form.get("user_name")
        gh_username = self.form.get("github_username_contact")
        email = self.form.get("email")
        linkedin = self.form.get("linkedin")

        if user_name:
            self.contact += f'<img align="left" src="https://avatars.githubusercontent.com/{gh_username}?size=100">\n\n'
            self.contact += f"Made with ❤️ by [{user_name}](https://github.com/{gh_username}), get in touch!\n\n"

        if email:
            self.contact += f'<a href="mailto:{email}" target="_blank">'
            self.contact += f'<img src="https://img.shields.io/badge/{email}-D14836?style=flat&logo=gmail&logoColor=white" alt="Email Badge" height="25"></a>&nbsp;\n'

        if linkedin:
            self.contact += (
                f'<a href="https://www.linkedin.com/in/{linkedin}" target="_blank">'
            )
            self.contact += f'<img src="https://img.shields.io/badge/{linkedin}-0077B5?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn Badge" height="25"></a>&nbsp;\n'

        if self.contact != "":
            self.contact = f'## Contact\n{self.contact}\n<br clear="left"/>\n'

    def add_skills(self):
        skills_name = self.form.getlist("skill_name")

        if skills_name:
            self.skills += "## Tech Stack\n"
            for skill in skills_name:
                self.skills += (
                    '<img src="'
                    + self.form.get(skill)
                    + '" alt="'
                    + skill
                    + ' Badge" height="25">&nbsp;\n'
                )
        self.skills += "\n"

    def add_index(self):
        self.index = '<p align="center">\n'

        if self.about:
            self.index += '\t<a href="#about">About</a> •\n'

        if self.features:
            self.index += '\t<a href="#features">Features</a> •\n'

        if self.skills:
            self.index += '\t<a href="#tech-stack">Tech Stack</a> •\n'

        if self.install:
            self.index += '\t<a href="#installation">Installation</a> •\n'

        if self.usage:
            self.index += '\t<a href="#usage">Usage</a> • \n'

        if self.contact:
            self.index += '\t<a href="#contact">Contact</a> •\n'

        # Remove last character (•)
        self.index = self.index[:-2]

        self.index += "\n</p>\n\n"
