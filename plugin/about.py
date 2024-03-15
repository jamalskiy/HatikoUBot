import asyncio

async def handle_about_command(event):

    reply_text=f'''
О проекте HatikoUBot:

1. Разработчик: @abanentick2
2. Исходный код: https://github.com/jamalskiy/HatikoUBot
3. ТГК: @HatikoUserBot
4. Версия: {version}


Что планируется сделать в будущем:

1. Удобное управление группами (для администраторов)
2. Проверка на обновление.
3. Круги из видео.
4. Установка видео по ссылке с YouTube Shorts и ТТ
        '''
    return reply_text