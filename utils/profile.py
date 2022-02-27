from application import db


def display_socials(user_info):
    markdown = ""
    social_medias = db.execute("SELECT name, badge, link FROM social_medias")

    for i in range(len(user_info)):
        if user_info[i]:
            link_social_media = social_medias[i]["link"].replace(
                "username", user_info[i]
            )
            link_badge = social_medias[i]["badge"].replace(
                social_medias[i]["name"], user_info[i]
            )

            markdown += f'<a href="{link_social_media}" target="_blank"><img src="{link_badge}" alt="{social_medias[i]["name"]} Badge" height="25"></a>&nbsp;\n'

    return markdown + "\n"


def display_about_you(prefix, info, prefix_links, info_links):
    markdown = ""

    for i in range(len(info)):
        if info[i]:
            emoji = prefix[i][:1]
            before_info = emoji + "&nbsp;" + prefix[i][2:]

            # Add new section with first info if not added
            if markdown == "":
                markdown += "## About me\n"
                markdown += before_info + " **" + info[i] + "**\n"
            else:
                markdown += "<br/>" + before_info + " **" + info[i] + "**\n"

    # Handle inputs with links
    for i in range(len(info_links)):
        link = str(info_links[i])
        if link != "":
            emoji = prefix_links[i][:1]
            before_info = emoji + "&nbsp;" + prefix_links[i][2:]

            if link.find("www") != -1:
                pre_link = "https://"
            else:
                pre_link = "mailto:"

            # Add new section with first info if not added
            if markdown == "":
                markdown += "## About me\n"
                markdown += before_info + " [" + link + "](" + pre_link + link + ")\n"
            else:
                markdown += (
                    "<br/>" + before_info + " [" + link + "](" + pre_link + link + ")\n"
                )

    return markdown + "\n"


def display_features_profile(form):
    markdown = ""

    features = ["gh_status_", "gh_top_languages_", "gh_streak_stats_"]

    for feature in features:
        if form.get(f"{feature}check") == "true":
            markdown += '<img height="180em" src="' + form.get(f"{feature}url") + '">\n'

    # Add new section if at least one option was selected
    return (
        ("## GitHub Analytics\n" + "<div>\n" + markdown + "</div>") if markdown else ""
    )
