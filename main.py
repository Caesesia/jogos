from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

import os
import discord

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = ".", intents = intents, help_command = None)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} au rapport.')
    #await bot.load_extension("")
    #await bot.load_extension("")
    #await bot.load_extension("")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

    if message.content.startswith(bot.command_prefix):
        return



bot.run(TOKEN)
