# bot.py
import os
import random

from discord.ext import commands
from discord.utils import get
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

@bot.command(name='role', help='adds role if it exits. Use: !role Dota')
async def dota_time(ctx, *arg):

    whitelist = (
        'test',
        'one two'
    )
    
    server = ctx.guild.id
    sRoles = bot.get_guild(server).roles
    
    if (arg):
        argStr = ' '.join(arg)
        tst = 0
        for x in range(len(sRoles)):
            if sRoles[x].name == argStr:
                tst = 1
                if sRoles[x].name in whitelist:
                    user = ctx.author
                    if (sRoles[x] not in user.roles):
                        await user.add_roles(sRoles[x])
                        response = (user.mention + ' is now a member of ' + sRoles[x].name)
                        await ctx.send(response)
                    else:
                        await user.remove_roles(sRoles[x])
                        response = (user.mention + ' is no longer a member of ' + sRoles[x].name)
                        await ctx.send(response)
                else:
                    await ctx.send("This role is not whitelisted")
        if (x+1 >= len(sRoles) and tst == 0):
            await ctx.send("This role does not exist")
    else:
        roleStr = " \n".join(whitelist)
        await ctx.send(ctx.author.mention + ", use !role (role) to assign yourself a role.\n"
                       "The following roles are self assignable:\n```"
                       + roleStr + "```")

bot.run(token)
bot.users
