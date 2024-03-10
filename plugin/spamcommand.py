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

async def handle_spam_command(event):
    try:
        user_id = event.sender_id

        if event.sender_id == user_id:

            _, repetitions, *text = event.text.split(' ')
            repetitions = int(repetitions)

            message_text = ' '.join(text)

            for _ in range(repetitions):
                await event.respond(message_text)
                await asyncio.sleep(0.07)
            
    except ValueError:
        await event.respond("Некорректные аргументы.\n\nПример: .spam 6 Hatiko")
