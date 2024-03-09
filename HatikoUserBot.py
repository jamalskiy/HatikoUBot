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

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("number")
client = TelegramClient('random', api_id, api_hash)
userid = os.getenv("user_id")

from datetime import datetime

@client.on(events.NewMessage(pattern='^🦔$', outgoing=True))
async def handler(event: events.NewMessage.Event):
    for i in range(19):
        await event.edit('🍎'*(18 - i) + '🦔')
        await asyncio.sleep(.5) # Задержка в секундах(0.5 стандарт)

@client.on(events.NewMessage(pattern='.scan'))
async def handler(event: events.NewMessage.Event):
    try:
        msg = await event.message.get_reply_message()
        try:
            sender_name = f'{msg.sender.title}'
        except:
            sender_name = f'{msg.sender.first_name} {msg.sender.last_name}'

        reply_text = f'┌ Информация о сканировании:\n'\
                     f'├ Имя пользователя: @{msg.sender.username}\n'\
                     f'├ ID пользователя: {msg.sender.id}\n'\
                     f'├ Полное имя: {sender_name}\n'\
                     f'├ Чат ID: {event.chat_id}\n'\
                     f'└ ID сообщения: {event._message_id}'


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
                await asyncio.sleep(0.07)   # Задержка в секундах
            
    except ValueError:
        await event.respond("Некорректные аргументы.\n\nПример: .spam 6 я спамер")

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
async def handle_hi_command(event: events.NewMessage.Event):
    user_id = event.sender_id
    message = '''Доступные команды:

1) .moon - стандарт обычная луна.
2) .moon ваш текст.
3) .spam (кол-во сообщений) (любой ваш текст) - (вводить без скоб).
4) .animate - анимация из сердечек.
5) .ты гуль? - спам 1000 - 7.
'''
    texti = "попьём чай с конфетами ☕️🍬? "
    text = message + texti

    await event.edit(text)

@client.on(events.NewMessage(pattern=r'^\.ты гуль\?', outgoing=True))
async def you_goul(event):
    number = 1000
    while number >= 13:
        await event.respond(f"{number} - 7 = {number - 7}")
        number -= 7
        await asyncio.sleep(0.09)


client.start(phone=phone_number)

client.run_until_disconnected()