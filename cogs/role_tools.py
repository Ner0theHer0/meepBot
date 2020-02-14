#role_tools.py

import discord
from discord.ext import commands

class role_tools():
    def init(self, bot):
        self.bot = bot

    @bot.command(name='role', help='adds role if it exits. Use: !role Dota', commands_heading='Roles')
    async def dota_time(ctx, *arg):

        whitelist = (
            'test',
            'one two'
        )
        
        server = ctx.guild.id
        sRoles = bot.get_guild(server).roles
        
        if (arg):
            argStr = ' '.join(arg)
            for x in range(len(sRoles)):
                if sRoles[x].name == argStr:
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

def setup(bot):
    bot.add_cog(role_tools(bot))
