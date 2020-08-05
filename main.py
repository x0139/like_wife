import random
from time import sleep

from instabot import Bot

from settings import USERNAME, PASSWORD, WIFE_ACCOUNT, COMMENTS

LAST_POSTS_COUNT = 10

SLEEP_TIMEOUT = 30 * 60  # half hour


def like_and_comment_my_wife(username: str, password: str, user_id: str, comments: list, last_commented: list,
                             comments_enabled=False) -> list:
    bot = Bot()
    bot.login(username=username, password=password)

    bot.like_user(user_id, filtration=False)

    if not comments_enabled:
        return last_commented

    medias = bot.get_last_user_medias(WIFE_ACCOUNT, LAST_POSTS_COUNT)
    not_commented = set(medias) - set(last_commented)
    for media_id in not_commented:
        if not bot.is_commented(media_id):
            comment = random.choice(comments)
            bot.comment(media_id, comment)
        last_commented.append(media_id)

    return last_commented[-LAST_POSTS_COUNT:]


if __name__ == '__main__':
    last_commented_medias = []

    while True:
        last_commented_medias = like_and_comment_my_wife(
            username=USERNAME,
            password=PASSWORD,
            user_id=WIFE_ACCOUNT,
            comments=COMMENTS,
            last_commented=last_commented_medias
        )

        sleep(SLEEP_TIMEOUT)
