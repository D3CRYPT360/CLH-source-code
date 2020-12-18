import discord
from discord import Embed
from discord.ext import commands, tasks
import sys, traceback
from itertools import cycle
import platform
import datetime
import asyncio
from dotenv import load_dotenv
import os
import json

load_dotenv('.env')

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = False)
bot = commands.Bot(command_prefix = '/', case_insensitive=True , intents = intents)
bot.remove_command('help')

loop = cycle(['/help for help', 'constant = sova', 'playing VALORANT', 'omen is an octopus'])

bot.version = "10.5"

@tasks.loop(seconds=60)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(loop)))

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="VALORANT"))
    print('Bot Online!')




initial_extensions = ['agents.agentlore',
                      'agents.cards',
                      'extras.help',
                      'extras.misc',
                      'agents.beta',
                      'agents.agentmaps',
                      'extras.owner',
                      'extras.eastereggs',
                      'extras.mods',
                      'extras.api',
                      'maps.maps',
                      'maps.time',

                      ]


if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'failed to load extention {extension}', file=sys.stderr)
            traceback.print_exc()


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def stats(ctx):
  pythonVersion = platform.python_version()
  dpyVersion = discord.__version__
  serverCount = len(bot.guilds)
  memberCount = len(set(bot.get_all_members()))

  embed = discord.Embed(title=f'{bot.user.name} Stats', description='\uFEFF', colour=ctx.author.colour, timestamp=ctx.message.created_at)

  embed.add_field(name='Bot Version:', value=bot.version)
  embed.add_field(name='Python Version:', value=pythonVersion)
  embed.add_field(name='Discord.py Version', value=dpyVersion)
  embed.add_field(name='Total Guilds:', value=serverCount)
  embed.add_field(name='Total Users:', value=memberCount)
  embed.add_field(name='Bot Developers:', value="<@482179909633048597>\n<@563361513281421313>")


  embed.set_footer(text=f"( ͡° ͜ʖ ͡°) | {bot.user.name}")
  embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
  embed.set_thumbnail(url=bot.user.avatar_url)

  await ctx.send(embed=embed)


async def online():
    await bot.wait_until_ready()
    channel = bot.get_channel(int(745696342260711516))
    await channel.send("<a:PETTHECONSTANT:758226856566063114>")
    await asyncio.sleep(10)


bot.load_extension("jishaku")
bot.run(os.getenv('DISCORD_TOKEN'))
