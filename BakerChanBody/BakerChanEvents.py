import BakerChanData as Data
import discord
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(ctx):
        MainChannel = ctx.bot.get_channel(734882609863065630)
        await MainChannel.send(Data.Messages.Get('on_ready'))
        await ctx.bot.change_presence(status = discord.Status.online, activity = discord.Game(Data.Messages.Get('activity')))
        print(f"\n{Data.Messages.Get('on_ready')}\n")
        print("-----------------------------------------Logs:")

    @commands.Cog.listener()
    async def on_member_join(ctx, member):
        print("{member} has joined the server.")
        
    @commands.Cog.listener()
    async def on_member_remove(ctx, member):
        print("{member} has left the server.")

def setup(bot):
    bot.add_cog(Events(bot))
    print(f"Loaded Cog: {Events.__name__}")
