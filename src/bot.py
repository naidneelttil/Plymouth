import discord
import os # default module
from dotenv import load_dotenv

## you need pycord and dotenv installed through pip or poetry, or whatever your package management system is. 

load_dotenv() # load all the variables from the env file
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

bot.run(os.getenv('TOKEN')) # run the bot with the token
