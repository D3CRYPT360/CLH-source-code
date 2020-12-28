import discord
from discord.ext import commands
import asyncio
from utils.maps_def import map_hex, lore_link_general, lore_link_scrapped, lore_link_unconfirmed, maps_codename, maps_real
from utils.requesting import Maps

class maps(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def map(self, ctx, map):
        json_data = Maps()
        maps = map.capitalize()
        for i in range(len(json_data['data'])):
            if json_data['data'][i]['displayName'] == maps: 
                embed = discord.Embed(
                    colour= map_hex(maps),
                    title = "__{} Lore:__".format(json_data['data'][i]['displayName']),
                    description="[Click for General Lore]({})".format(lore_link_general(maps)) + "\n[Click for Unconfirmed Lore]({})".format(lore_link_unconfirmed(maps)) + "\n[Click for Scrapped Lore]({})".format(lore_link_scrapped(maps))
                )
                embed.set_image(url="{}".format(json_data['data'][i]['listViewIcon'])),
                embed.add_field(name="__{} Info:__".format(json_data['data'][i]['displayName']),value="```\nCodename: {}\nLocation: {}\nCoordinates: {}```".format(maps_codename(maps), maps_real(maps), json_data['data'][i]['coordinates'])),     
                await ctx.send(embed=embed)
    
    @commands.command(aliases=['ascent', 'icebox', 'haven', 'split'])
    async def bind(self, ctx):
        await ctx.send("Command has changed to `/map [mapName]` without the []", delete_after=5)
                

def setup(bot):
    bot.add_cog(maps(bot))
    print('Maps.py loaded')
