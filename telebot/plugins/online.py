# Copyright TeleBot
# For @TeleBotHelp coded by @xditya
# Kangers keep credits else I'll take down š§

import random
import sys

from telethon import version

from telebot import ALIVE_NAME
from telebot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "TeleBot User"

ONLINESTR = [
    "āāāāāāāāāāāāāāāāāāāā \nāāā¦āā¦āāā¦āāāāāāā¦āāāāā  āāāāāā āāāāāāāāāāā āāā \nāāāā©āāāāāāāāāā©āā©āāāā \nāāāāāāāāāāāāāāāāāāāā \n\n**TeleBot is online.**\n\n**All systems functioning normally !** \n\n**Bot by** [Aditya š®š³](tg://user?id=719195224) \n\n**More help -** @TeleBotHelpChat \n\n           [š§ GitHub Repository š§](https://github.com/xditya/TeleBot)",
    f"ā¦āā¦āāā¦āāāāāāā¦āāā\nāāāā āāāāāāāāāāā ā\nāā©āāāāāāāāāā©āā©āā\n              **Welcome to TeleBot**\n\n**Hey master! I'm alive. All systems online and functioning normally ā**\n\n**āļø Telethon version:** `{version.__version__}` \n\n**āļø Python:** `{sys.version}` \n\nāļø More info: @TeleBotHelpChat \n\nāļø Created by: [Aditya š®š³](tg://user?id=719195224) \n\n**āļø Database status:** All ok š \n\n**āļø My master:** {DEFAULTUSER} \n\n        [š Github repository š](https://github.com/xditya/TeleBot)",
]


@telebot.on(admin_cmd(outgoing=True, pattern="online"))
@telebot.on(sudo_cmd(allow_sudo=True, pattern="online"))
async def online(event):
    """ Greet everyone! """
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await eor(event, random.choice(ONLINESTR))
