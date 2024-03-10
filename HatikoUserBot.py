'''
Автор кода: Jamalskiy
Телеграмм канал: @HatikoUserBot
Версия кода: 0.0.1


Обратная связь:
Telegram: @abanentick2

Либо можете задать вопрос в GitHub: 
https://github.com/jamalskiy/HatikoUBot
'''

from telethon.sync import TelegramClient, events
import asyncio
import re
from datetime import datetime
import importlib
from importlib import util
from telethon.tl import types
import os
from dotenv import load_dotenv
from plugin import *

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("number")
userid = os.getenv("user_id")

client = TelegramClient('random', api_id, api_hash)

@client.on(events.NewMessage(pattern='^🦔$', outgoing=True))
async def minimulti_handler(event: events.NewMessage.Event):
    await handle_minimulti_command(event)

@client.on(events.NewMessage(pattern='.scan'))
async def scan_handler(event: events.NewMessage.Event):
    msg = await event.message.get_reply_message()
    reply_text = await handle_scan_command(event, msg)
    await event.edit(reply_text)

@client.on(events.NewMessage(pattern='.spam'))
async def spam_handler(event: events.NewMessage.Event):
    await handle_spam_command(event, userid)

@client.on(events.NewMessage(pattern=r'^\.ты гуль\?', outgoing=True))
async def goul_handler(event: events.NewMessage.Event):
    await handle_goul_command(event)

@client.on(events.NewMessage(pattern='.moon'))
async def moon_command_handler(event: events.NewMessage.Event):
    await handle_moon_command(event, userid)

@client.on(events.NewMessage(pattern=r'^\❤️ magick'))
async def animation_command_handler(event: events.NewMessage.Event):
    await handle_animation_command(event, userid)


@client.on(events.NewMessage(pattern=r'^\.команды'))
async def helpcommand(event: events.NewMessage.Event):
    reply_text = await help_command(event)
    await event.edit(reply_text)

client.start(phone=phone_number)
client.run_until_disconnected()