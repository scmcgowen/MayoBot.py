import discord, json

# Channel IDs:
# support: 564187710512955402
# general: 564185633984348172
# Bot ID: 564362414770880512


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        if message.channel.id == 565499722635280404 and message.content.startswith('!a '):
            await message.add_reaction('\U0001f44d')
            await message.add_reaction('\U0001f44e')
            await message.add_reaction('\U00002705')
        if message.channel.id != 565499722635280404 and message.channel.id != 565478348483067914:
            if message.content.startswith('?') or message.content.startswith('!'):
                await message.delete()
                await message.channel.send(message.author.mention + ": Please use <#565478348483067914> for bot commands.")

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



client = MyClient(activity=discord.Game(name='!help'))

client.run(open("token.txt", "r").read())
