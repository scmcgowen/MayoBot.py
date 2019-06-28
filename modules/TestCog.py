import discord

from discord.ext import commands


class TestCog(commands.Cog):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
