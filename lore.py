import discord
from discord import Embed
from discord.ext import commands, tasks
import sys, traceback
from itertools import cycle
import platform
import datetime
import asyncio
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import json

cwd = Path(__file__).parents[0]
cwd = str(cwd)
secret = json.load(open(cwd+'/configs/config.json'))

#PATCH CHECKER
link = "https://playvalorant.com/en-us/news/game-updates/valorant-patch-notes-1-13/"
s = BeautifulSoup(requests.get(link)._content, "lxml")
canonical = s.find('link', {'rel': 'canonical'})
result = canonical['href']

#UPDATE CHECKER
Dict = {}

url = "https://clientconfig.rpg.riotgames.com/api/v1/config/public?os=windows&app=Riot%20Client&patchline=KeystoneFoundationLiveWin"
r = requests.get(url)
json_data = r.json()
basepath = json_data["keystone.products.valorant.patchlines.live"]["platforms"]["win"]["configurations"]


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
    print('Cool')




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
                      'maps.split',
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
  embed.add_field(name='Bot Developer:', value="<@482179909633048597>")


  embed.set_footer(text=f"( ͡° ͜ʖ ͡°) | {bot.user.name}")
  embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
  embed.set_thumbnail(url=bot.user.avatar_url)

  await ctx.send(embed=embed)


async def online():
    await bot.wait_until_ready()
    channel = bot.get_channel(int(745696342260711516))
    await channel.send("<a:PETTHECONSTANT:758226856566063114>")
    await asyncio.sleep(10)

#Defining
@tasks.loop(seconds = 12.0) # running the task every 12 secs. 5 requests every 60 seconds
async def update():
    for index in range(len(basepath)):
        id = basepath[index]["id"]
        patch_url = basepath[index]["patch_url"].rsplit('/',1)[1].rsplit('.',1)[0]
        if(len(Dict) < len(basepath)):
            Dict[id] = patch_url # creating keys and setting base values
                    
        elif(Dict[id] != patch_url):
            channel = bot.get_channel(int(746327425759182908))
            if not any(x == patch_url for x in Dict.values()):
                await channel.send("--- New update [{}] ---".format([Dict[id]]))
                        
                Dict[id] = patch_url    # updating value of current region to new one
                await channel.send(f"{id} region has received update: <@482179909633048597>")
                if(all(x == Dict[id] for x in Dict.values())):
                    await channel.send(f"--- All regions received [{Dict[id]}] ---")
                    update.stop()
                
@update.before_loop
async def wait_for_bot(): #waiting for the bot to go online so it won't start the loop before it goes online
    await bot.wait_until_ready()

@bot.command()
async def dict(ctx):
    await ctx.send(Dict)

@bot.command(aliases=["restart"])
@commands.is_owner()
async def reset(ctx):
    update.restart()
    await ctx.send("Patch Command has been restarted")


@tasks.loop(seconds=12.0)    
async def patch():
    if result == link:
        channel = bot.get_channel(int(746327425759182908))
        await channel.send(link + "\nNew Patch updated")
        patch.stop()


@patch.before_loop
async def wait(): #waiting for the bot to go online so it won't start the loop before it goes online
    await bot.wait_until_ready()
    
@bot.command()
async def debug(ctx):
    await ctx.send("The bot is currently looking for \n" + link)

update.start()
patch.start()
bot.load_extension("jishaku")
bot.run(secret['token'])
