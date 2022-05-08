from models import SocialMedia


class ProfileForm:
    def __init__(self, form):
        self.form = form
        self.markdown = ""

    def create_markdown(self):

        # Title/Name
        name = self.form.get("name")
        if name:
            self.markdown += "# " + name + "\n"

        self.add_social_medias()

        # Subtitle
        subtitle = self.form.get("subtitle")
        if subtitle:
            greet = self.form.get("greet")
            self.markdown += "## " + greet + "\n"
            self.markdown += subtitle + "\n\n"

        # Profile Views
        if self.form.get("gh_views_check") == "true":
            self.markdown += (
                "![Profile Views](" + self.form.get("profile_views_url") + ")\n\n"
            )

        self.add_about_you()
        self.add_skills()
        self.add_cool_features()

        return self.markdown

    # Add social media section
    def add_social_medias(self):
        user_info = self.form.getlist("social_media_input")

        social_medias = SocialMedia.query.filter_by(badge_type="with_username").all()

        for i, item in enumerate(user_info):
            if item:
                link_social_media = social_medias[i].social_link.replace(
                    "username", item
                )
                link_badge = social_medias[i].badge_link.replace(
                    social_medias[i].name, item
                )

                self.markdown += f'<a href="{link_social_media}" target="_blank"><img src="{link_badge}" alt="{social_medias[i].name} Badge" height="25"></a>&nbsp;\n'

        self.markdown += "\n"

    # Add about yout section
    def add_about_you(self):
        aux_markdown = ""
        prefix = self.form.getlist("about_you_prefix")
        info = self.form.getlist("about_you_input")

        for i, item in enumerate(info):
            if item:
                before_info = prefix[i][:1] + "&nbsp;" + prefix[i][2:]

                # Add new section with title first info (without <br>) if not added
                if aux_markdown == "":
                    aux_markdown += "## About me\n"
                    aux_markdown += before_info + " **" + item + "**\n"
                else:
                    aux_markdown += "<br/>" + before_info + " **" + item + "**\n"

        # Handle inputs with link

        # Email
        email = self.form.get("about_you_email_input")
        if email:
            prefix = self.form.get("about_you_email_prefix")
            before_info = prefix[:1] + "&nbsp;" + prefix[2:]

            # Add new section with title first info (without <br>) if not added
            if aux_markdown == "":
                aux_markdown += "## About me\n"
                aux_markdown += before_info + " [" + email + "](mailto:" + email + ")\n"
            else:
                aux_markdown += (
                    "<br/>" + before_info + " [" + email + "](mailto:" + email + ")\n"
                )

        # Portfolio link
        portfolio = self.form.get("about_you_portfolio_input")
        if portfolio:
            link = portfolio
            if not portfolio.startswith("www"):
                link = "www." + link

            prefix = self.form.get("about_you_portfolio_prefix")
            before_info = prefix[:1] + "&nbsp;" + prefix[2:]

            # Add new section with title first info (without <br>) if not added
            if aux_markdown == "":
                aux_markdown += "## About me\n"
                aux_markdown += before_info + " [" + portfolio + "](" + link + ")\n"
            else:
                aux_markdown += (
                    "<br/>" + before_info + " [" + portfolio + "](" + link + ")\n"
                )

        self.markdown += aux_markdown + "\n"

    # Add tech stack section
    def add_skills(self):
        skills_name = self.form.getlist("skill_name")

        if skills_name:
            self.markdown += "## Tech Stack\n"
            for skill in skills_name:
                self.markdown += (
                    '<img src="'
                    + self.form.get(skill)
                    + '" alt="'
                    + skill
                    + ' Badge" height="25">&nbsp;\n'
                )

        self.markdown += "\n"

    # add github features section
    def add_cool_features(self):
        aux_markdown = ""

        features = ["gh_status_", "gh_top_languages_", "gh_streak_stats_"]

        for feature in features:
            if self.form.get(f"{feature}check") == "true":
                aux_markdown += (
                    '<img height="180em" src="'
                    + self.form.get(f"{feature}url")
                    + '">\n'
                )

        # Add new section if at least one option was selected

        self.markdown += (
            ("## GitHub Analytics\n" + "<div>\n" + aux_markdown + "</div>")
            if aux_markdown
            else ""
        )
