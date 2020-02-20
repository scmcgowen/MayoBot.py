import importlib


import discord, json
from discord.ext import commands

from Config import get_token, get_module_names, get_modules
from CoreCog import CoreCog


bot = commands.Bot(command_prefix='s!')


@bot.event
async def on_ready():
    print('Logged on as: ', bot.user)
    await bot.get_guild(564185633984348170).get_channel(565478348483067914).send("👋  I'm back online!")
    await bot.change_presence(activity=discord.Game(name="?help"))


def setup():
    print(get_module_names())
    bot.add_cog(CoreCog(bot))
    load_modules()
    bot.run(get_token())


def load_modules():
    module_list = get_module_names()
    for module in module_list:
        my_module = importlib.import_module("modules.%s" % module)
        klass = getattr(my_module, module)
        bot.add_cog(klass(bot))



setup()
