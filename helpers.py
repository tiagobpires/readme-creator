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


# if __name__ == "__main__":
#     display_socials('hey','hey')
