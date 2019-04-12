import discord, json
from discord.ext import commands
from pprint import pprint

# Channel IDs:
# support: 564187710512955402
# general: 564185633984348172
# Bot ID: 564362414770880512
support_channel = 565499722635280404
botspam_channel = 565478348483067914



class MyClient(discord.Client):



    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if JsonHelper().is_muted(message.author.id):
            await message.delete()
            await message.channel.send(message.author.mention + ": You are muted, so you can't write in this guild! Don't try to bypass this punishment or you will get banned.")

        if message.content == 'ping':
            await message.channel.send('pong')

        if message.content == 'pong':
            await message.channel.send('ping')

        if message.channel.id != support_channel and message.channel.id != botspam_channel:
            if message.content.startswith('?') or message.content.startswith('!'):
                await message.delete()
                await message.channel.send(message.author.mention + ": Please use <#565478348483067914> for bot commands.")

        """~~~~~~~~COMMANDS~~~~~~~~"""

        # if message.channel.id == botspam_channel:
        #     if message.content.startswith('!a'):
        #         await message.add_reaction('\U0001f44d')  # thumbsup emoji
        #         await message.add_reaction('\U0001f44e')  # thumbsdown emoji
        #         await message.add_reaction('\U00002705')  # checkbox emoji
        #     #if message.content.startswith('!help'):
        #     #    await message.channel.send('Help feature will be added very soon.')
        #     if message.content.startswith('!mute'):
        #         JsonHelper().mute()


    async def on_reaction_add(self, reaction, user):
        if reaction.message.channel.id == 565499722635280404:
            if user.id == reaction.message.author.id:
                print('You cannot vote for yourself!')
                await reaction.remove(user)
            elif user.id == 564362414770880512:
                print('Reaction added by Bot!')
            else:
                print('Reaction added by user ' + user)
                # Add vote/downvote/solve to DB for user reaction.message.author
    async def on_reaction_remove(self, reaction, user):
        if reaction.message.channel.id == 565499722635280404:
            if user.id == 564362414770880512:
                print('Bot removed reaction.')
            else:
                pass
                # remove vote/downvote/solve from DB for user reaction.message.author
class JsonHelper:
    """Serves all strings & settings from the JSON database."""

    def get_points(self, user_id):
        """Returns the points of the user that belongs to the specified ID."""
        with open('database.json') as f:
            db = json.load(f)
            f.close()
        for attribute in db['users']:
            if attribute['id'] == user_id:
                return attribute['points']


    def get_blacklist(self):
        """Returns the whole blacklist."""
        with open('database.json') as f:
            db = json.load(f)
            f.close()
        return db['blacklist']


    def is_blacklisted(self, command):
        """Returns a boolean that describes the current blacklist state of a command."""
        with open('database.json') as f:
            db = json.load(f)
            f.close()
        for cmd in db['blacklist']:
            return cmd == command


    def add_to_blacklist(self, command):
        """Adds a command to the blacklist."""
        pass

    def remove_from_blacklist(self, command):
        """Removes a command from the blacklist."""
        pass

    def is_muted(self, user_id):
        """Returns a boolean that describes the current mute state of a user."""
        with open('database.json') as f:
            db = json.load(f)
            f.close()
        for attribute in db['users']:
            if attribute['id'] == user_id:
                return attribute['muted']


    def unmute(self, user_id):
        """Unmutes a user."""
        pass

    def mute(self, user_id):
        """Mutes a user."""
        pass



client = MyClient(activity=discord.Game(name='!help'))

client.run(open("token.txt").read())
