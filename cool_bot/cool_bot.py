import discord
import asyncio
from distutils.cmd import Command
from discord.ext import commands
import random
import os

from cogs.image_cog import image_cog

token = ""
with open("token.txt") as file:
    token = file.read()

bot = commands.Bot(intents=discord.Intents.all(),command_prefix = '//')
# bot.add_cog(image_cog(bot))

# @bot.event()
# async def on_ready():
#     print("Bot Online...")

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
async def main():
    await load()
    await bot.start(token)
asyncio.run(main())
    
    
asyncio.run(main())