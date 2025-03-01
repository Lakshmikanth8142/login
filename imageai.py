import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from aiogram import Bot, Dispatcher, types, F
import asyncio
import os
import logging

# Bot Token
TOKEN = "7939267224:AAGshWkCpI_6HVAsct4vH7rVQqzREXo3LQc"

# Logging
logging.basicConfig(level=logging.INFO)

# Check GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
precision = torch.float16 if device == "cuda" else torch.float32
print(f"[🔥] Device: {device}")

# Load Stable Diffusion Model
pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1",
    torch_dtype=precision
).to(device)

pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

# Telegram Bot Initialization
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Start Command
@dp.message(F.text.lower() == "/start")
async def start(message: types.Message):
    await message.reply("👋 Hello! Welcome to the **AI Image Generator Bot**.\nSend me any **text prompt** to generate an AI image 🔥.")

# Text Prompt Handler
@dp.message(F.text)
async def generate_image(message: types.Message):
    prompt = message.text
    await message.reply(f"✨ Generating Image for: `{prompt}`... Please wait...")

    try:
        # Generate Image
        image = pipe(prompt, width=512, height=512).images[0]
        filename = "image.jpg"
        image.save(filename, quality=85)

        # Send Image to User
        photo = types.FSInputFile(filename)
        await message.answer_photo(photo, caption=f"✅ Image for: `{prompt}`")

        # Delete Image after Sending
        os.remove(filename)

    except Exception as e:
        await message.reply("❌ Image generation failed! Please try again.")
        print(f"[ERROR] {e}")

async def main():
    print("[✅] Bot is Running...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, timeout=600)

if __name__ == "__main__":
    asyncio.run(main())
