#role_tools.py

import os
import random
import sys
import csv

from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
import discord


class Roles(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='role', help='Assigns you an available role')
    async def role_command(self, ctx, *arg):

        whitelist = []

        whitelist = read_csv('whitelist.csv')
        if whitelist is None:
            response = (user.mention + ', there are no whitelisted roles in this server')
            await ctx.send(response)
            return
        
        sRoles = ctx.guild.roles
        
        if (arg):
            argS = ' '.join(arg)
            argStr = argS.lower()
            for x in range(len(sRoles)):
                if sRoles[x].name.lower() == argStr:
                    if sRoles[x].name.lower() in whitelist:
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
            
        elif (whitelist):
            roleStr = " \n".join(whitelist)
            await ctx.send(ctx.author.mention + ", use !role (role) to assign yourself a role.\n"
                           "The following roles are self assignable:\n```"
                           + roleStr + "```")
        else:
            await ctx.send("There are currently no self-assignable roles")

    @commands.command(name='whitelist', help='Whitelists a role')
    async def add_to_whitelist(self, ctx, *arg):
        
        if not ctx.author.guild_permissions.administrator:
            await ctx.send("Only and administrator can perform this action")
            
        elif (arg):
            argS = ' '.join(arg)
            argStr = argS.lower()

            whitelist = []
            whitelist = read_csv('whitelist.csv')

            with open('whitelist.csv', 'w', newline='') as wl:

                sRoles = ctx.guild.roles

                for z in range(len(sRoles)):
                    if sRoles[z].name.lower() == argStr:
                        
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
        else:
            
            whitelist = []
            whitelist = read_csv('whitelist.csv')
            
            if (whitelist):
                roleStr = " \n".join(whitelist)
                await ctx.send(ctx.author.mention + ", the following roles are self assignable:\n```"
                           + roleStr + "```")
            else:
                await ctx.send("There are currently no whitelisted roles")
    
def read_csv(filename):
            with open(filename) as wl:
                read = csv.reader(wl)

                wlist = []
                col = 0
                for row in read:
                    try:
                        wlist.append(row[0])
                    except:
                        print("No roles are in the whitelist")
                return wlist
            
def setup(bot):
    bot.add_cog(Roles(bot))
    
