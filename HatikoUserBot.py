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

from datetime import datetime

@client.on(events.NewMessage(pattern='^🦔$', outgoing=True))
async def handler(event: events.NewMessage.Event):
    for i in range(19):
        await event.edit('🍎'*(18 - i) + '🦔')
        await asyncio.sleep(.5)

@client.on(events.NewMessage(pattern='.scan'))
async def handler(event: events.NewMessage.Event):
    try:
        msg = await event.message.get_reply_message()
        reply_text = await handle_scan_command(event, msg)
    except Exception as e:
        print(e)
        reply_text = f"Ошибка: {e}"

    await event.edit(reply_text)

@client.on(events.NewMessage(pattern='.spam'))
async def repeat_message(event):
    try:
        if event.sender_id == userid:
            user_id = event.sender_id

            _, repetitions, *text = event.text.split(' ')
            repetitions = int(repetitions)

            message_text = ' '.join(text)

            for _ in range(repetitions):
                await event.respond(message_text)
                await asyncio.sleep(0.07)
            
    except ValueError:
        await event.respond("Некорректные аргументы.\n\nПример: .spam 6 Hatiko")

@client.on(events.NewMessage(pattern='.moon'))
async def handle_moon_command(event: events.NewMessage.Event):
    user_id = event.sender_id

    if event.sender_id == userid:
        user_text = event.text[len('.moon') + 1:].strip()
        moon_sequence = [
            '🌖 ',
            '🌗',
            '🌘 ',
            '🌑',
            '🌒 ',
            '🌒',
            '🌓 ',
            '🌔',
        ]

        for _ in range(13):  # 13 повторов
            for moon in moon_sequence:
                message = ""
                

                if user_text:
                    message += user_text + " "
                    message += moon
                else:
                    message += moon
                await client.edit_message(event.chat_id, event.message.id, message)
                await asyncio.sleep(0.9)   # Задержка в секундах между кадрами анимации


async def read_frames_from_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read().decode('utf-8')
            frames = re.findall(r"'''(.*?)'''", content, re.DOTALL)
        return frames
    except FileNotFoundError:
        return None

async def display_animation(event, frames):
    for frame in frames:
        await event.edit(frame)
        await asyncio.sleep(EDIT_DELAY)

@client.on(events.NewMessage(pattern=r'^\.animate'))
async def handle_animation_command(event):
    file_path = 'magick.py'
    user_id = event.sender_id

    if event.sender_id == userid:
        frames = await read_frames_from_file(file_path)
        if frames:
            for frame in frames:
                await event.edit(frame)
                await asyncio.sleep(0.25)   # Задержка в секундах между кадрами анимации

@client.on(events.NewMessage(pattern=r'^\.команды'))
async def helpcommand(event: events.NewMessage.Event):
    reply_text = await help_command(event)
    await event.edit(reply_text)

@client.on(events.NewMessage(pattern=r'^\.ты гуль\?', outgoing=True))
async def you_goul(event):
    number = 1000
    while number >= 13:
        await event.respond(f"{number} - 7 = {number - 7}")
        number -= 7
        await asyncio.sleep(0.09)


client.start(phone=phone_number)

client.run_until_disconnected()