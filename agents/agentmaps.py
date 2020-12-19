import discord
from discord.ext import commands

class AgentMaps(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['sargeorg' , 'brimorg'])
    async def brimstoneorg(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blurple(),
            title='Brimstone Origin'
        )
        embed.set_image(url="https://media.discordapp.net/attachments/747484591836758127/749233385003679834/Home_Brimstone.PNG?width=852&height=499")
        embed.add_field(name="USA", value="Brimstone is from USA.The Brazilian launch trailer showed a graphic of the grand canyon behind him. He also has a military background.", inline=True)
        await ctx.send(embed=embed)


    #viper#
    @commands.command(aliases = ['sabineorg' , 'pandemicorg'])
    async def viperorg(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blurple(),
            title='Viper Origin'
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/727811131254505523/750991887447621692/Viper_is_Alaskan.jpg")
        embed.add_field(name="Alaska,USA", value="Viper comes from Alaska USA this is where she grew up and later in life 2 significant events happend in her life 1: She was in New York Near the world Trade center while 2: is the 'one dark night' card where she is in Seattle USA. Riot PHRISK confirmed she is from alaska.", inline=True)
        await ctx.send(embed=embed)

    #Omen#
    @commands.command(aliases = ['wraithorg'])
    async def omenorg(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blurple(),
            title='Viper Origin'
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/727811131254505523/750991887447621692/Viper_is_Alaskan.jpg")
        embed.add_field(name="Alaska,USA", value="Viper comes from Alaska USA this is where she grew up and later in life 2 significant events happend in her life 1: She was in New York Near the world Trade center while 2: is the 'one dark night' card where she is in Seattle USA. Riot PHRISK confirmed she is from alaska.", inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AgentMaps(bot))
    print('Agentmaps.py loaded')
