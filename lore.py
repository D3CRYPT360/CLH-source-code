import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv('.env')

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = False)
bot = commands.Bot(command_prefix = '/', case_insensitive=True , intents = intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="VALORANT"))
    print('Bot Online!')

for filename in os.listdir('./agents'):
    if filename.endswith('.py'):
        bot.load_extension(f'agents.{filename[:-3]}')
for filename in os.listdir('./extras'):
    if filename.endswith('.py'):
        bot.load_extension(f'extras.{filename[:-3]}')
for filename in os.listdir('./maps'):
    if filename.endswith('.py'):
        bot.load_extension(f'maps.{filename[:-3]}')

bot.load_extension("jishaku")
bot.run(os.getenv('DISCORD_TOKEN'))