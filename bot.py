from discord.ext import commands
from discord.utils import get
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

description = 'Bringing the FUN in disfunction'

default_extensions = ["role_tools", "misc"]

bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as ' +
          str(bot.user.name) + " " +
          str(bot.user.id))

@bot.command(name="load", help="Loads an extention")
async def load(ctx, extention : str):
    try:
        bot.load_extension(extension)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.send("{} loaded.".format(extension))

@bot.command(name="unload", help="Unloads an extention")
async def unload(ctx, extension : str):
    bot.unload_extension(extension)
    await ctx.send("{} unloaded.".format(extension))

@bot.command(name='add', help="Adds two numbers")
async def add_smth(ctx, int1 : int, int2 : int):
    await ctx.send(int1 + int2)

if __name__ == "__main__":
    for extension in default_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(token)
