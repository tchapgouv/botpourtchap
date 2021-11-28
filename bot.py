# echo.py
# Example:
# randomuser - "!echo example string"
# echo_bot - "example string"

import os
import simplematrixbotlib as botlib

MATRIX_HOME_SERVER=os.environ["MATRIX_HOME_SERVER"]
MATRIX_BOT_USERNAME=os.environ["MATRIX_BOT_USERNAME"]
MATRIX_BOT_PASSWORD=os.environ["MATRIX_BOT_PASSWORD"]

creds = botlib.Creds(MATRIX_HOME_SERVER,MATRIX_BOT_USERNAME,MATRIX_BOT_PASSWORD)
bot = botlib.Bot(creds)
PREFIX = '!'

@bot.listener.on_message_event
async def ping(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and match.command("ping"):

        await bot.api.send_text_message(
            room.room_id, "pong"
            )

bot.run()
