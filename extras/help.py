import discord
from discord.ext import commands
from disputils import BotEmbedPaginator

class __Help__(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(case_insensitive=True)
    async def help(self, ctx):
        p1 = discord.Embed(title="__HELP COMMAND__\n`prefix = /`" , color=0xFF4654, inline=True)
        p1.set_thumbnail(url='https://cdn.discordapp.com/avatars/750160303169470486/9d86482f1f4d6b19263e4aa1ea3142d8.png?size=256')
        p1.add_field(name="For Agent Lore", value="`/(agent name)`\neg. `/cypher`")
        p1.add_field(name="For Agent cards", value="`/card (agent name)`\neg. `/card jett`")
        p1.add_field(name="Rift Lore", value="`/rift`")
        p1.add_field(name="For Beta Agent cards", value="`/beta (agent name) only one beta agents`\neg. `/beta jett`")
        p1.add_field(name="Misc commands", value="`Nitro` - free nitro updated everyday\n`agents` - Total Agents in Valorant\n`languages` - languages supported by valorant\n`fox` - cute foxes\n`region` - To check if a region's server is down (BETA)\n`cats`,`dogs` - to see random pictures of them", inline=False)
        p1.set_footer(text="more coming soon :D")
        await ctx.send(embed=p1)

def setup(bot):
    bot.add_cog(__Help__(bot))
    print('Help is Ready')
