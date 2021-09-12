import requests
from pyrogram import Client as Bot
from pyrogram import idle

from ZeroTwo.config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN
from ZeroTwo.services.callsmusic.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="ZeroTwo.modules"),
)

bot.start()
run()
idle()
