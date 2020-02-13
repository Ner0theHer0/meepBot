# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='kalpa', help='insults Kalpa')
async def fuck_kalpa(ctx):
    hate = [
        '<@!217583229165633536> shits in gutters',
        '<@!217583229165633536> = inferior engineer',
    ]

    response = random.choice(hate)
    await ctx.send(response)

@bot.command(name='dota', help='pings @Dota')
async def dota_time(ctx):
    response = ("<@&677373582082310154>\n"
    "ITS TIME FOR DOTA NERDS\n"
    "<@&677373582082310154>\n"
    "<@&677373582082310154>")
    await ctx.send(response)

@bot.command(name='flip', help='flips a coin')
async def coin_flip(ctx):
    result = [
        'Heads',
        'Tails',
    ]
    response = random.choice(result)
    await ctx.send(response)

bot.run(token)
bot.users
