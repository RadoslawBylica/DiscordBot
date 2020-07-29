import discord
import BakerChanData as Data
from discord.ext import commands
from os import path, chdir, listdir

if __name__  == "__main__":
    Data.init(path.dirname(path.abspath(__file__)))
    chdir(Data.Settings.MainPath)
    bot = commands.Bot(command_prefix = Data.Settings.Prefix)
    print("-----------------Cogs Loading-----------------")
    for FileName in listdir(Data.Settings.BodyPath):
        if FileName.endswith(".py"):
            try:
                bot.load_extension(f"{Data.Settings.BodyName}.{str(FileName).strip('.py')}")
            except Exception as ErrorMessage:
                print(ErrorMessage)
    print("----------------------------------------------")
    ModersIDs = [363473001779298304]

    async def WhoCanModerate(ctx):
        try:
            ModersIDs.index(ctx.author.id)
        except ValueError:
            return False
        else:
            return True

    @bot.command()
    @commands.check(WhoCanModerate)
    async def Language(ctx, Language:str):
        Data.Messages.ChangeLanguage(Language)

    @bot.command()
    @commands.check(WhoCanModerate)
    async def OpenExtension(ctx, *, ExtensionName:str):
        try:
            bot.load_extension(f"{Data.Settings.BodyName}.{ExtensionName}")
        except Exception as ErrorMessage:
            await ctx.send(ErrorMessage)
            print(ErrorMessage)
        else:
            await ctx.send(Data.Messages.Get('OpenExtension'))
            print(Data.Messages.Get('OpenExtension'))

    @bot.command()
    @commands.check(WhoCanModerate)
    async def CloseExtension(ctx, *, ExtensionName:str):
        try:
            bot.unload_extension(f"{Data.Settings.BodyName}.{ExtensionName}")
        except Exception as ErrorMessage:
            await ctx.send(ErrorMessage)
            print(ErrorMessage)
        else:
            await ctx.send(Data.Messages.Get('CloseExtension'))
            print(Data.Messages.Get('CloseExtension'))

    @bot.command()
    @commands.check(WhoCanModerate)
    async def RestartExtension(ctx, *, ExtensionName:str):
        try:
            bot.unload_extension(f"{Data.Settings.BodyName}.{ExtensionName}")
            bot.load_extension(f"{Data.Settings.BodyName}.{ExtensionName}")
        except Exception as ErrorMessage:
            await ctx.send(ErrorMessage)
            print(ErrorMessage)
        else:
            await ctx.send(Data.Messages.Get('RestartExtension'))
            print(Data.Messages.Get('RestartExtension'))

    @OpenExtension.error
    @CloseExtension.error
    @RestartExtension.error
    async def CheckFailure(ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(Data.Messages.Get('CheckFailure'))

    bot.run(Data.Settings.Token)
