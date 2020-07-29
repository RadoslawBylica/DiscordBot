import os
import discord
from discord.utils import get
from discord.ext import commands

async def ConnectBotToChannel(bot, ctx, ChannelToConnect = None):
    BotVoice = get(bot.voice_clients, guild=ctx.guild)
    if ChannelToConnect == None:
        UserVoice = ctx.author.voice
        if UserVoice == None:
            raise Exception(f"{ctx.member.nick} nie znajdujesz się na kanale głowosym, ani nie podałeś kanału do połączenia się.")
        if BotVoice and BotVoice.is_connected():
            await BotVoice.move_to(UserVoice.channel)
        else:
            await UserVoice.channel.connect()
    else:
        await ChannelToConnect.connect()

async def DisconnectBot(bot, ctx):
    await (get(bot.voice_clients, guild=ctx.guild)).disconnect()