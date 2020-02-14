# bot.py
import os
import random

from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', description="I bring the FUN in disfunction!")

@bot.command(name='kalpa', help='insults Kalpa')
async def fuck_kalpa(ctx):
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

def setup(bot):
    bot.add_cog(Members(bot))

@bot.command(name='dota', help='pings @Dota', commands_heading='General')
async def dota_time(ctx):

    server = ctx.guild.id
    sRoles = bot.get_guild(server).roles
    
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

@bot.command(name='flip', help='flips a coin', commands_heading='General')
async def coin_flip(ctx):
    result = [
        'Heads',
        'Tails',
    ]
    response = random.choice(result)
    await ctx.send(response)

@bot.command(name='git', help='Links to github repo')
async def git_post(ctx):
    response = 'Find the source code for this bot here: https://github.com/Ner0theHer0/meepBot'
    await ctx.send(response)

@bot.command(name='role', help='adds role if it exits. Use: !role Dota', commands_heading='Roles')
async def dota_time(ctx, *arg):

    whitelist = (
        'test',
        'one two',
        'dota'
    )
    
    server = ctx.guild.id
    sRoles = bot.get_guild(server).roles
    
    if (arg):
        argStr = ' '.join(arg)
        for x in range(len(sRoles)):
            if sRoles[x].name == argStr.lower():
                if sRoles[x].name in whitelist:
                    user = ctx.author
                    if (sRoles[x] not in user.roles):
                        await user.add_roles(sRoles[x])
                        response = (user.mention + ' is now a member of ' + sRoles[x].name)
                        await ctx.send(response)
                        return
                    else:
                        await user.remove_roles(sRoles[x])
                        response = (user.mention + ' is no longer a member of ' + sRoles[x].name)
                        await ctx.send(response)
                        return
                    
                else:
                    await ctx.send("This role is not whitelisted")
                    return
                
        await ctx.send("This role does not exist")
        
    else:
        roleStr = " \n".join(whitelist)
        await ctx.send(ctx.author.mention + ", use !role (role) to assign yourself a role.\n"
                       "The following roles are self assignable:\n```"
                       + roleStr + "```")

bot.run(token)
bot.users
