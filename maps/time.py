import discord
from discord.ext import commands

class Map(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #firstlight#
    @commands.command(aliases = ['light' , 'first'])
    async def firstlight(self, ctx):
        embed = discord.Embed(
            colour=0xFF4654,
            title=("**First light date probably 2050:**")
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/747040395891966002/747048503699570688/First_Light_4x.png")
        embed.add_field(name = "__First Light Info__", value="```(after first light):... certain people around the world end up with new hyper-natural powers... These new powers brought about massive global changes, including the rise of new governments. Eventually in response to the events that occur around First Light, a new organization called VALORANT is created by secretive backers.```", inline=True)
        await ctx.send(embed=embed)

    #Duelist#
    @commands.command()
    async def duelist(self, ctx):
        embed = discord.Embed(
            colour=0xFF4654,
            title=("**Duelist Cinematic happened in the Year 2049:**")
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/747040395891966002/747048776027603014/Duelists_time_line.JPG")
        await ctx.send(embed=embed)

    #Map Code#
    @commands.command()
    async def codes(self, ctx):
        embed = discord.Embed(
            colour=0xFF4654
        )
        embed.add_field(name = "Map codes", value="```-Duality == Bind\n-Bonsai == Split\n-Triad == Haven\n-Venice == Ascent\n-Port == Icebox\n-The Range == Poveglia```")
        await ctx.send(embed=embed)





def setup(bot):
    bot.add_cog(Map(bot))
    print('Time.py loaded')
