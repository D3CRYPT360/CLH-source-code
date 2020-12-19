import discord
from discord.ext import commands
import requests

thumbnail = "https://cdn.discordapp.com/avatars/514418193364942850/7c56b3712cd14ae3db6c8593c5f23cf5.png?size=256"


class Down(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def status(self, ctx, region):
        region = region.lower()
        r = requests.get(f"https://valorant.secure.dyn.riotcdn.net/channels/public/x/status/{region}.json")
        if r.status_code == 200:
            riot = r.json()
            
                            
            if (riot['incidents']) == [] and (riot['maintenances']) == [] :# If there is no incidents/maintenance
                await ctx.send ("No recent issues or events reported")
                    
            
            elif (riot['maintenances'])!= []:# If the issue is related to a maintenance
                embed = discord.Embed(
                    colour = discord.Colour.dark_gold(),
                    title=(riot["maintenances"][0]['titles'][0]['content'])
                )
                embed.add_field(name = (riot['maintenances'][0]['updates'][0]['created_at'][:10]), value=(riot['maintenances'][0]['updates'][0]['translations'][0]['content']))
                embed.set_thumbnail(url=thumbnail)
                await ctx.send(embed=embed)
                
            elif (riot['incidents']) != []:# If the issue is related to an incident
                embed = discord.Embed(
                    colour = discord.Colour.dark_gold(),
                    title=(riot["incidents"][0]['titles'][0]['content'])
                )
                embed.add_field(name = (riot['incidents'][0]['updates'][0]['created_at'][:10]), value=(riot['incidents'][0]['updates'][0]['translations'][0]['content']))
                embed.set_thumbnail(url=thumbnail)
                await ctx.send(embed=embed)
                    
            if (riot['maintenances']) and (riot['incidents']) != []: # If there is both a maintenance and an incident  
                embed1 = discord.Embed(
                    colour = discord.Colour.dark_gold(),
                    title=(riot["maintenances"][0]['titles'][0]['content'])
                )
                embed1.add_field(name = (riot['maintenances'][0]['updates'][0]['created_at'][:10]), value=(riot['maintenances'][0]['updates'][0]['translations'][0]['content']))
                embed1.set_thumbnail(url=thumbnail)
                
                embed2 = discord.Embed(
                    colour = discord.Colour.dark_gold(),
                    title=(riot["incidents"][0]['titles'][0]['content'])
                )
                embed2.add_field(name = (riot['incidents'][0]['updates'][0]['created_at'][:10]), value=(riot['incidents'][0]['updates'][0]['translations'][0]['content']))
                embed2.set_thumbnail(url=thumbnail)
                await ctx.send(embed=embed1)
                await ctx.send(embed=embed2)
            
    
        elif r.status_code != 200:
            await ctx.send(f"{region} server status not found...")
        

    
            
    
def setup(bot):
    bot.add_cog(Down(bot))
    print('Api.py loaded')