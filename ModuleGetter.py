import importlib
import urllib.request

import discord
import requests
from discord.ext import commands


def download_module(url: str, name: str):
    urllib.request.urlretrieve(url, './modules/' + name + '.py')


def check_module(name: str) -> str:

    klass = []
    try:
        my_module = importlib.import_module("modules.%s" % name)
        klass = getattr(my_module, name)

        if issubclass(klass, commands.Cog):
            print("Successfully loaded module %s." % name)
            return "fine"
        else:
            print("Couldn't load module/class %s: Module does not extend to 'commands.Cog'" % name)
            return "Module does not extend to 'commands.Cog'"

    except ModuleNotFoundError as e:
        print("Couldn't load module/class %s: ModuleNotFoundError" % name)
        print(str(e))
        return str(e)
    except AttributeError as e:
        print("Couldn't load module/class %s: AttributeError" % name)
        print(str(e))
        return str(e)
    except:
        print("Couldn't load module/class %s: Couldn't determine Error." % name)
        return "err"
