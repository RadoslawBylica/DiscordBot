import discord
from discord.ext import commands

class Errors(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Taka komenda nie istnieje.")
        else:
            await ctx.send(error)

def setup(bot):
    bot.add_cog(Errors(bot))
    print(f"Loaded Cog: {Errors.__name__}")
