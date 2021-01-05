import discord
from discord.ext import commands
from valoStatus import Region

thumbnail = "https://cdn.discordapp.com/avatars/514418193364942850/7c56b3712cd14ae3db6c8593c5f23cf5.png?size=256"


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
                await ctx.send(embed=embed)
                
            elif region.maintenence_check() == True:
                embed = discord.Embed(
                    colour = discord.Colour.orange(),
                    title = region.maintenances_title()
                )
                embed.add_field(name=region.maintenances_date(), value=region.maintenances_reason())
                await ctx.send(embed=embed)
                
            elif region.maintenence_check() == True and region.incident_check() == True:
                embed1 = discord.Embed(
                    colour = discord.Colour.orange(),
                    title = region.incidents_title()
                )
                embed1.add_field(name=region.incidents_date(), value=region.incidents_reason())
                await ctx.send(embed=embed1)
                
                embed2 = discord.Embed(
                    colour = discord.Colour.orange(),
                    title = region.maintenances_title()
                )
                embed2.add_field(name=region.maintenances_date(), value=region.maintenances_reason())
                await ctx.send(embed=embed2)

    
            
    
def setup(bot):
    bot.add_cog(Down(bot))
    print('Api.py loaded')