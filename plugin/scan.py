async def handle_scan_command(event, msg, user_id):
    try:

        if event.sender_id == user_id:
            if not msg:
                return "Надо отвечать на сообщения."

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

    return reply_text

