#admin.py

import os
import random
import sys

from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
import discord

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='exit', help='Sends the bot offline')
    async def go_offline(self, ctx):
        if (ctx.author.guild_permissions.administrator):
            response = "Goodnight!"
            await ctx.send(response)
            sys.exit(0)
        else:
            response = "Only an admin can perform this action"
            await ctx.send(response)

def setup(bot):
    bot.add_cog(Admin(bot))
