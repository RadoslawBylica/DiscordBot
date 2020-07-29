import os
import random
import discord
import BakerChanData as Data
from discord.utils import get
from discord.ext import commands

class Comands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{Data.Messages.Get('ping')} {round(self.bot.latency * 1000)}ms.")

    @commands.command(aliases = ["wyczysc"])	
    async def clear(self, ctx, amount:int = 1):
        if amount <= 0:
            await ctx.send(f"{Data.Messages.Get('clear')}")
        else:
            await ctx.channel.purge(limit = amount + 1)

    @commands.command(aliases = ["przenies"])
    async def move(self, ctx, member:discord.Member, *, channel:discord.VoiceChannel):
        await member.move_to(channel)

def setup(bot):
    bot.add_cog(Comands(bot))
    print(f"Loaded Cog: {Comands.__name__}")