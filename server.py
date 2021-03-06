import ntpath
import os
from bot import telegram_chatbot
import gizoogle

path = os.getcwd() + '\\config.cfg'
config_name = ntpath.basename(path)

bot = telegram_chatbot(config_name)


# bot = telegram_chatbot("config.cfg")


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


def make_reply(msg):
    reply = None
    if msg is not None:
        reply = reverse(msg)
        # reply = gizoogle.text(msg)
    return reply


update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            # try:
            if 'channel_post' in item:
                if 'text' in item['channel_post']:
                    message = str(item["channel_post"]["text"])
                else:
                    message = str(item["channel_post"]["sticker"])
            else:
                if 'text' in item['message']:
                    message = str(item["message"]["text"])
                else:
                    message = str(item["message"]["sticker"])

            # except:
            #   message = "ok"
            try:
                from_ = item["message"]["from"]["id"]
            except:
                from_ = item["channel_post"]["chat"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
