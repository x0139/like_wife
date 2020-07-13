from time import sleep

from instabot import Bot

from settings import USERNAME, PASSWORD

if __name__ == '__main__':
    wife_account = 'alise_artemova'
    bot = Bot()
    bot.login(username=USERNAME, password=PASSWORD)
    while True:
        bot.like_user(wife_account, filtration=None)
        sleep(1800)
