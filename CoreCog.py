import importlib
import subprocess
import sys

import discord
from discord.ext import commands

from Config import add_module, get_module_names, remove_module
from ModuleGetter import download_module, check_module


class CoreCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def module(self, ctx, action, name=None, url=None):
        if ctx.message.author.id == 218444620051251200:
            if action == "add":
                download_module(url, name)

                check = check_module(name)

                if check == "fine":
                    await ctx.send("⬇ |   Module '%s' was downloaded successfully and checked. No errors found! Enabling module..." % name)
                    add_module(name)
                    my_module = importlib.import_module("modules.%s" % name)
                    klass = getattr(my_module, name)
                    self.bot.add_cog(klass(self.bot))
                    await ctx.send("✅ |   Module '%s' was enabled!" % name)
                elif check == "err":
                    await ctx.send("🚫 |   Module '%s' was downloaded successfully but check failed. Error is undefined." % name)
                else:
                    await ctx.send("🚫 |   Module '%s' was downloaded successfully but check failed.\nError:%s" % (name, check))
            elif action == "remove":
                # TODO remove actual file
                if name:
                    remove_module(name)
                    await ctx.send("✅ |   Module '%s' was removed!" % name)
                else:
                    await ctx.send("🚫 |   Please specify the name of the module you want to remove.")
            elif action == "list":
                await ctx.send(get_module_names())
            elif action == "show":
                pass
            else:
                await ctx.send("🚫 |   Invalid action. Valid actions are: add, remove, enable, disable, list, show")
        else:
            await ctx.send("🚫 |   Only my overlord, realmayus is permitted to execute this command.")

    @commands.command()
    async def pip(self, ctx, action, package):
        if ctx.message.author.id == 218444620051251200:
            if action == "install":
                output = subprocess.check_output([sys.executable, "-m", "pip", "install", package])
                await ctx.send("✅ |   I told `pip` to install '%s'. That's the command output:\n```%s```" % (package, output))
            elif action == "uninstall":
                output = subprocess.check_output([sys.executable, "-m", "pip", "uninstall", "-y", package])
                await ctx.send("✅ |   I told `pip` to uninstall '%s'. That's the command output:\n```%s```" % (package, output))


        else:
            await ctx.send("🚫 |   Only my overlord, realmayus is permitted to execute this command.")
