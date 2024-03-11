import asyncio

async def about(event):
    user_id = event.sender_id

    if event.sender_id == user_id:
        message='''
О проекте HatikoUBot:

1. Разработчик: @abanentick2
2. Исходный код: https://github.com/jamalskiy/HatikoUBot
3. ТГК: @HatikoUserBot
4. Версия: 0.0.3


Что планируется сделать в будущем:

1. Удобное управление группами (для администраторов)
2. Проверка на обновление.
3. Круги из видео.
4. Установка видео по ссылке с YouTube Shorts и ТТ
        '''
        await event.edit(message)