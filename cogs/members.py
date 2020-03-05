#members.py

import os
import random
import sys
import csv

from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
import discord

class Memebers(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kalpa', help='Insults Kalpa')
    async def fuck_kalpa(self, ctx):
        hate = [
            '<@!217583229165633536> shits in gutters',
            '<@!217583229165633536> = inferior engineer',
        ]

        kalpa = 217583229165633536
        
        if (ctx.guild.get_member(kalpa)):
            response = random.choice(hate)
            await ctx.send(response)
        else:
            await ctx.send("Kalpa isn't here to hate on!")

    @commands.command(name='dota', help='Pings @Dota')
    async def dota_time(self, ctx):

        sRoles = ctx.guild.roles
        
        for x in range(len(sRoles)):
            if sRoles[x].name.lower() == "dota":
                response = (sRoles[x].mention + "\n" +
                sRoles[x].mention + "\n" +
                "ITS TIME FOR DOTA NERDS\n" +
                sRoles[x].mention + "\n" +
                sRoles[x].mention)
                await ctx.send(response)
                return
        response = ("There isn't a dota role on this server :sob:")
        await ctx.send(response)

    @commands.command(name='git', help='Links to github repo')
    async def git_post(self, ctx):
        response = 'Find the source code for this bot here: https://github.com/Ner0theHer0/meepBot'
        await ctx.send(response)

    @commands.command(name='flip', help='Flips a coin')
    async def coin_flip(self, ctx):
        result = [
            'Heads',
            'Tails',
        ]
        response = random.choice(result)
        await ctx.send(response)

def setup(bot):
    bot.add_cog(Memebers(bot))
