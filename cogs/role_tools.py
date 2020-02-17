#role_tools.py

import os
import random
import sys
import csv

from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
import discord

import csv


class role_toolsCog(commands.Cog):

    #bot = commands.Bot(command_prefix='!', description="I bring the FUN in disfunction!")

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='role', help='adds role if it exits. Use: !role Dota', pass_context = True)
    async def role_command(self, ctx, *arg):

        whitelist = []

        whitelist = read_csv('whitelist.csv')

        #server = ctx.guild.id
        sRoles = ctx.guild.roles
        
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

    @commands.command(name='whitelist', help='whitelists a role')
    async def add_to_whitelist(self, ctx, *arg):
        
        if not ctx.author.guild_permissions.administrator:
            await ctx.send("Only and administrator can perform this action")
            
        else:
            argStr = ' '.join(arg)
            argStr.lower()
            
            whitelist = []
            whitelist = read_csv('whitelist.csv')

            with open('whitelist.csv', 'w', newline='') as wl:

                server = ctx.guild.id
                sRoles = ctx.guild.roles

                for z in range(len(sRoles)):
                    if sRoles[z].name.lower() in argStr:
                        
                        write = csv.writer(wl,  delimiter=' ')
                        
                        if argStr in whitelist:
                            whitelist.remove(argStr)
                            await ctx.send("Removed role '" + argStr + "' from whitelist")

                        else:
                            write.writerow([argStr])
                            await ctx.send("Whitelisted role '" + argStr + "'")

                        for x in range(len(whitelist)):
                            write.writerow([whitelist[x]])
                        return
                await ctx.send("Role '" + argStr + "' does not exist")
    
def read_csv(filename):
            with open(filename) as wl:
                read = csv.reader(wl)

                wlist = []
                col = 0
                for row in read:
                    wlist.append(row[0])
                return wlist
            
def setup(bot):
    bot.add_cog(role_toolsCog(bot))
    
