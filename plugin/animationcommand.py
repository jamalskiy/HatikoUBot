import asyncio

async def handle_animation_command(event, userid):
    file_path = 'magick.py'
    user_id = event.sender_id

    if event.sender_id == userid:
        frames = await read_frames_from_file(file_path)
        if frames:
            for frame in frames:
                await event.edit(frame)
                await asyncio.sleep(0.25)
