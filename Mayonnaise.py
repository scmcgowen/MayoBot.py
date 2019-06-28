import importlib
from pprint import pprint

import discord, json
from discord.ext import commands

from Config import get_token, get_module_names
from CoreCog import CoreCog
from ModuleGetter import download_module, check_module

bot = commands.Bot(command_prefix='?')

bot.remove_command('help')


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
        my_module = importlib.import_module(name='.' + module, package='modules')
        klass = getattr(my_module, module)
        bot.add_cog(klass(bot))


setup()
