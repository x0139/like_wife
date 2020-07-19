from time import sleep

from instabot import Bot

from settings import USERNAME, PASSWORD, WIFE_ACCOUNT


def like_my_wife(username, password, user_id):
    bot = Bot()
    bot.login(username=username, password=password)
    bot.like_user(user_id, filtration=False)


if __name__ == '__main__':
    while True:
        like_my_wife(username=USERNAME, password=PASSWORD, user_id=WIFE_ACCOUNT)
        sleep(1800)
