async def handle_help_command(event):
    user_id = event.sender_id

    if event.sender_id == user_id:
        message = '''Доступные команды:

1) .moon - стандарт обычная луна.
2) .moon ваш текст.
3) .spam (кол-во сообщений) (любой ваш текст) - (вводить без скоб).
4) .animate - анимация из сердечек.
5) .ты гуль? - спам 1000 - 7.
6) 🦔 - минимультик
7) .scan - информация о сообщении (для разработчиков)
'''
        texti = "попьём чай с конфетами ☕️🍬? "
        text = message + texti
        return text
