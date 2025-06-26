import discord
from discord.ext import commands
import random
import string
import os  # for environment variables

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=',', intents=intents)

def generate_code(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

@bot.event
async def on_ready():
    print(f'✅ Bot is online as {bot.user}')

@bot.command()
async def code(ctx):
    random_code = generate_code()
    await ctx.send(f'🎲 Your random code is: `{random_code}`')

bot.run(TOKEN)

