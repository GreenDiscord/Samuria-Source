import discord
from discord.ext import commands
import os
from help import Help

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="s#", intents=intents, help_command=Help(), case_insensitive=True)
bot.co = bot.get_command("help")
bot.co.hidden = True


@bot.event
async def on_ready():
    for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

    bot.description = f"Mod Bot used in {len(bot.guilds)}"
    print(f"We have logged in as {bot.user} and watching {len(bot.guilds)} guilds :)")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name =f"roblox"))
    print("Discord.py version? " + discord.__version__)

@bot.event
async def on_message(message):
    lis = ["fuck", "FUCK", "Fuck", "shit", "Shit", "SHIT"]
    try:
        if message.content in lis:
             await message.delete()
             await message.channel.send(f"Hi, Dont say that :) ({message.author.mention} just said a blacklisted word)")
    except commands.MissingPermissions:
        pass
    
    await bot.process_commands(message)
    

@bot.command()
async def hi(ctx):
    """Just A note, this command will stay if the cogs dont load"""
    await ctx.send(f"Hi {ctx.author.mention} :)")


bot.run("ODA1ODQ0MjIyMzcyNDc5MDE2.YBgy6g.As8Wf5s3z4IgtFVTooE02MDl-Uo")