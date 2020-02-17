import discord
from discord.ext import commands

from dotenv import load_dotenv
import os

import sys
import traceback

initial_extensions = [
    'cogs.role_tools'
    #'cogs.members',
    #'cogs.admin'
]

bot = commands.Bot(command_prefix='!', description="I bring the FUN in disfunction!")

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot.run(token)
