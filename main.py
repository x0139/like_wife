import random
from time import sleep

from instabot import Bot

from settings import USERNAME, PASSWORD, WIFE_ACCOUNT, COMMENTS_FILE

LAST_POSTS_COUNT = 10

SLEEP_TIMEOUT = 30 * 60  # half hour


def like_and_comment_my_wife(username: str, password: str, user_id: str, comment: str, last_commented: list) -> list:
    bot = Bot()
    bot.login(username=username, password=password)

    bot.like_user(user_id, filtration=False)

    medias = bot.get_last_user_medias(WIFE_ACCOUNT, LAST_POSTS_COUNT)
    not_commented = set(medias) - set(last_commented)
    for media_id in not_commented:
        if not bot.is_commented(media_id):
            bot.comment(media_id, comment)
        last_commented.append(media_id)

    return last_commented[-LAST_POSTS_COUNT:]


if __name__ == '__main__':
    last_commented_medias = []

    with open(COMMENTS_FILE, 'r') as f:
        lines = [x.strip('\n') for x in f.readlines()]
        comments = [x for x in lines if x]

    while True:
        last_commented_medias = like_and_comment_my_wife(
            username=USERNAME,
            password=PASSWORD,
            user_id=WIFE_ACCOUNT,
            comment=random.choice(comments),
            last_commented=last_commented_medias
        )

        sleep(SLEEP_TIMEOUT)
