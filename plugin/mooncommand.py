import asyncio

async def handle_moon_command(event):
    user_text = event.text[len('.moon') + 1:].strip()
    moon_sequence = [
        '🌖',
        '🌗',
        '🌘',
        '🌑',
        '🌒',
        '🌒',
        '🌓',
        '🌔',
    ]

    for _ in range(13):
        for moon in moon_sequence:
            message = ""
            if user_text:
                message += user_text + " " + moon
            else:
                message += "Сладких снов ❤️"+ moon + "❤️"
            await event.edit(message)
            await asyncio.sleep(0.9)