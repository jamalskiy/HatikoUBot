import asyncio

async def handle_minimulti_command(event, user_id):
    if event.sender_id == user_id:
        for i in range(19):
            await event.edit('🍎'*(18 - i) + '🦔')
            await asyncio.sleep(.5)
