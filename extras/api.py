import discord
from discord.ext import commands
from valoStatus import Region

thumbnail = "https://cdn.discordapp.com/attachments/745696342260711516/797394997698756638/Valorant.v2.png"

class Down(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def status(self, ctx, region):
        region = Region(region)
        if region.get_status_issue() == False:
            await ctx.send("No recent issues or incidents reported")
        else:
            if region.incident_check() == True:
                embed = discord.Embed(
                    colour = discord.Colour.orange(),
                    title = region.incidents_title()
                )
                embed.add_field(name=region.incidents_date(), value=region.incidents_reason())
                embed.set_thumbnail(url=thumbnail)
                await ctx.send(embed=embed)
                
            elif region.maintenence_check() == True:
                embed = discord.Embed(
                    colour = discord.Colour.orange(),
                    title = region.maintenances_title()
                )
                embed.add_field(name=region.maintenances_date(), value=region.maintenances_reason())
                embed.set_thumbnail(url=thumbnail)
                await ctx.send(embed=embed)
                
            elif region.maintenence_check() == True and region.incident_check() == True:
                embed1 = discord.Embed(
                    colour = discord.Colour.orange(),
                    title = region.incidents_title()
                )
                embed1.add_field(name=region.incidents_date(), value=region.incidents_reason())
                embed1.set_thumbnail(url=thumbnail)
                await ctx.send(embed=embed1)
                
                embed2 = discord.Embed(
                    colour = discord.Colour.orange(),
                    title = region.maintenances_title()
                )
                embed2.add_field(name=region.maintenances_date(), value=region.maintenances_reason())
                embed2.set_thumbnail(url=thumbnail)
                await ctx.send(embed=embed2)

    
            
    
def setup(bot):
    bot.add_cog(Down(bot))
    print('Api.py loaded')
