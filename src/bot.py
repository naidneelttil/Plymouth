import discord
from discord.ext import commands
import os # default module
from dotenv import load_dotenv

## you need pycord and dotenv installed through pip or poetry, or whatever your package management system is. 

intents = discord.Intents.default()
intents.message_content = True
load_dotenv() # load all the variables from the env file
bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

@bot.command()
async def role(ctx, *, message):
    await ctx.send("you hit a role command, yippie! **{}**".format(message))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Unknown command.")

bot.run(os.getenv('TOKEN')) # run the bot with the token
