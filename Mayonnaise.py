import discord, json
from discord.ext import commands
from pprint import pprint

from database import JsonHelper

support_channel = 565499722635280404
botspam_channel = 565478348483067914

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)

bot.remove_command('help')


@bot.event
async def on_ready():
    print('Logged on as', bot.user)

@bot.event
async def on_message(message):
    # don't respond to ourselves
    if message.author == bot.user:
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
            return

    await bot.process_commands(message)
    # if message.channel.id == botspam_channel:
    #     if message.content.startswith('!a'):
    #         await message.add_reaction('\U0001f44d')  # thumbsup emoji
    #         await message.add_reaction('\U0001f44e')  # thumbsdown emoji
    #         await message.add_reaction('\U00002705')  # checkbox emoji
    #     #if message.content.startswith('!help'):
    #     #    await message.channel.send('Help feature will be added very soon.')
    #     if message.content.startswith('!mute'):
    #         JsonHelper().mute()
#
# @bot.event
# async def on_reaction_add(reaction, user):
#     if reaction.message.channel.id == 565499722635280404:
#         if user.id == reaction.message.author.id:
#             print('You cannot vote for yourself!')
#             await reaction.remove(user)
#         elif user.id == 564362414770880512:
#             print('Reaction added by Bot!')
#         else:
#             print('Reaction added by user ' + user)
#             # Add vote/downvote/solve to DB for user reaction.message.author
#
# @bot.event
# async def on_reaction_remove(reaction, user):
#     if reaction.message.channel.id == 565499722635280404:
#         if user.id == 564362414770880512:
#             print('Bot removed reaction.')
#         else:
#             pass
#             # remove vote/downvote/solve from DB for user reaction.message.author

@bot.command()
async def foo(ctx, *, rest):
    await ctx.send(rest)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Command help", url="https://github.com/MayusYT/MayoBot.py", color=0x36df9a)
    embed.set_author(name="MayoBot", icon_url = "https://cdn.discordapp.com/icons/564185633984348170/554e16d35e14ab2fb0ef00ba80d6442c.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/564185633984348170/554e16d35e14ab2fb0ef00ba80d6442c.png")
    embed.add_field(name='!a', value = 'Send an answer to a question. Bot reacts with voting buttons that others can click to upvote you.See  #info for more information about roles.', inline=False)
    embed.add_field(name='!help', value='Show this help panel', inline=True)
    embed.add_field(name='!stats <@User>', value='Shows a stats embed for the specified user.If no one is defined, the stats of you will be displayed.', inline=True)
    embed.add_field(name='!vk[@User]', value='Votekicks the specified user.', inline=True)
    embed.set_footer(text="MayoBot is licensed under MIT license.")
    await ctx.send(embed=embed)
bot.run(open("token.txt").read())
