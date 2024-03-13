'''
Автор кода: Jamalskiy
Телеграмм канал: @HatikoUserBot
Версия кода: 0.0.3


Обратная связь:
Telegram: @abanentick2

Либо можете задать вопрос в GitHub: 
https://github.com/jamalskiy/HatikoUBot
'''

import sqlite3
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
user_id = os.getenv("userid")

client = TelegramClient('random', api_id, api_hash)

@client.on(events.NewMessage(pattern=re.compile(r'^\!(еж|ёж|ежик|ёжик)', re.IGNORECASE)))
async def minimulti_handler(event: events.NewMessage.Event):
    await handle_minimulti_command(event, user_id)

@client.on(events.NewMessage(pattern=re.compile(r'^\!(scan|скан)', re.IGNORECASE)))
async def scan_handler(event: events.NewMessage.Event):
    msg = await event.message.get_reply_message()
    reply_text = await handle_scan_command(event, msg, user_id)
    await event.edit(reply_text)

@client.on(events.NewMessage(pattern=re.compile(r'^\!(spam|спам)', re.IGNORECASE)))
async def spam_handler(event: events.NewMessage.Event):
    await handle_spam_command(event, user_id)

@client.on(events.NewMessage(pattern=r'^\!ты гуль\?', outgoing=True))
async def goul_handler(event: events.NewMessage.Event):
    await handle_goul_command(event, user_id)

@client.on(events.NewMessage(pattern=re.compile(r'^\!(moon|луна)', re.IGNORECASE)))
async def moon_command_handler(event: events.NewMessage.Event):
    await handle_moon_command(event, user_id)

@client.on(events.NewMessage(pattern=re.compile(r'^(❤️ magick|❤️ магия)', re.IGNORECASE)))
async def animation_command_handler(event: events.NewMessage.Event):
    await handle_animation_command(event, user_id)

@client.on(events.NewMessage(pattern=re.compile(r'^\!(команды|команда|хелп)', re.IGNORECASE)))
async def helpcommand(event: events.NewMessage.Event):
    reply_text = await handle_help_command(event, user_id)
    await event.edit(reply_text)

@client.on(events.NewMessage(pattern=re.compile(r'^\!(about|о проекте)', re.IGNORECASE)))
async def about(event: events.NewMessage.Event):
    reply_text = await about(event, user_id)
    await event.edit(reply_text)

client.start(phone=phone_number)
client.run_until_disconnected()