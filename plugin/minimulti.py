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

async def handle_minimulti_command(event):
    user_id = event.sender_id

    if event.sender_id == user_id:
        for i in range(19):
            await event.edit('🍎'*(18 - i) + '🦔')
            await asyncio.sleep(.5)
