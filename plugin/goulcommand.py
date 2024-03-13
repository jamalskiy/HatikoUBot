import asyncio

async def handle_goul_command(event, user_id):
    if event.sender_id == user_id:
        number = 1000
        while number >= 13:
            await event.respond(f"{number} - 7 = {number - 7}")
            number -= 7
            await asyncio.sleep(0.09)
