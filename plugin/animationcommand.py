'''
Автор кода: Jamalskiy
Телеграмм канал: @HatikoUserBot
Версия кода: 0.0.1


Обратная связь:
Telegram: @abanentick2

Либо можете задать вопрос в GitHub: 
https://github.com/jamalskiy/HatikoUBot
'''

import asyncio
import re

async def read_frames_from_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read().decode('utf-8')
            frames = re.findall(r"'''(.*?)'''", content, re.DOTALL)
        return frames
    except FileNotFoundError:
        return None

async def handle_animation_command(event):
    file_path = 'magick.py'
    user_id = event.sender_id

    if event.sender_id == user_id:
        frames = await read_frames_from_file(file_path)
        if frames:
            for frame in frames:
                await event.edit(frame)
                await asyncio.sleep(0.25)
