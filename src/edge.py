import asyncio
import edge_tts

async def main():
    text = "ສະບາຍດີ, ມື້ນີ້ເຈົ້າສຸກສະບາຍດີບໍ?"
    voice = "lo-LA-KeomanyNeural"  # Lao female voice

    tts = edge_tts.Communicate(text, voice)
    await tts.save("lao_voice_long.mp3")
    print("✅ Saved Lao speech to lao_voice.mp3")

asyncio.run(main())
