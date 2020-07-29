import BakerChanData as Data
import youtube_dl
import discord
from discord.utils import get
from discord.ext import commands
from os import path, chdir, rename

from BakerChanFunctions import ConnectBotToChannel, DisconnectBot

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
            
    @commands.command(aliases = ["wejdz"])
    async def join(self, ctx, *, ChannelToConnect:discord.VoiceChannel = None):
        try:
            await ConnectBotToChannel(self.bot, ctx, ChannelToConnect)
        except Exception as ErrorLog:
            await ctx.send(ErrorLog)
            print(ErrorLog)
  
    @commands.command(aliases = ["wyjdz"])
    async def leave(self, ctx):
        await DisconnectBot(self.bot, ctx)

    @commands.command()
    async def SecretSovietFunction(self, ctx, member:discord.Member):
        pass

    @commands.command(aliases = ["graj"])
    async def play(self, ctx, *, name:str):
        try:
            await ConnectBotToChannel(self.bot, ctx)
        except Exception as ErrorLog:
            await ctx.send(ErrorLog)
            print(ErrorLog)
        SongPath = path.join(Data.Settings.SongsFolder, name + ".mp3")
        BotVoice = get(self.bot.voice_clients, guild=ctx.guild)
        if path.isfile(SongPath):
            BotVoice.play(discord.FFmpegPCMAudio(SongPath))
            BotVoice.source = discord.PCMVolumeTransformer(BotVoice.source)
            BotVoice.source.volume = 0.01
        else:
            await ctx.send(f"{Data.Messages.Get('play')}")

    @commands.command(aliases = ["glosnosc"])
    async def volume(self, ctx, volume:float = 0.01):
        (get(self.bot.voice_clients, guild=ctx.guild)).source.volume = volume

    @commands.command(aliases = ["wznow"])
    async def resume(self, ctx, volume:float = 0.01):
        BotVoice = get(self.bot.voice_clients, guild=ctx.guild)
        if not(BotVoice.is_playing()):
            BotVoice.resume()
    
    @commands.command(aliases = ["przestan"])
    async def stop(self, ctx, volume:float = 0.01):
        (get(self.bot.voice_clients, guild=ctx.guild)).stop()


    @commands.command(aliases = ["wstrzymaj"])
    async def pause(self, ctx, volume:float = 0.01):
        BotVoice = get(self.bot.voice_clients, guild=ctx.guild)
        if BotVoice.is_playing():
            BotVoice.pause()


    @commands.command(aliases = ["Download", "youtube", "Youtube", "yt", "Yt"])
    async def download(self, ctx, url:str, *, name = None):
        if name != None:
            SongPath = path.join(Data.Settings.SongsFolder, name + ".mp3")
            if path.isfile(SongPath):
                ctx.send(Data.Messages.Get('download1'))
            else:
                ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{ 'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192', }],
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    chdir(SongsFolder)
                    try:
                        info = ydl.extract_info(url, download=True)
                        SongName = (str(ydl.prepare_filename(info)).strip(".webm")) + ".mp3"
                        if path.isfile(SongName):
                            rename(SongName, name + ".mp3")
                    except FileNotFoundError as e:
                        print(e)
                    finally:
                        chdir("..")                      
        else:
            await ctx.send(Data.Messages.Get('download2'))

def setup(bot):
    bot.add_cog(Music(bot))
    print(f"Loaded Cog: {Music.__name__}")
