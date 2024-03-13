import asyncio

async def handle_spam_command(event, user_id):
    try:

        if event.sender_id == user_id:

            _, repetitions, *text = event.text.split(' ')
            repetitions = int(repetitions)

            message_text = ' '.join(text)

            for _ in range(repetitions):
                await event.respond(message_text)
                await asyncio.sleep(0.07)
            
    except ValueError:
        await event.respond("Некорректные аргументы.\n\nПример: .spam 6 Hatiko")
