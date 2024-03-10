import asyncio

async def handle_moon_command(event, userid):
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

        for _ in range(13):
            for moon in moon_sequence:
                message = ""
                
                if user_text:
                    message += user_text + " "
                    message += moon
                else:
                    message += moon
                await client.edit_message(event.chat_id, event.message.id, message)
                await asyncio.sleep(0.9)
