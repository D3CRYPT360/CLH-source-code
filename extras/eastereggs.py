import discord
from discord.ext import commands
import requests

class Egg(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def jeff(self, ctx):
        await ctx.send("<:hi:759981685671460894>")

    @commands.command()
    async def bababooey(self, ctx):
        await ctx.send("https://tenor.com/view/imma-see-you-tomorrow-bye-slip-gif-15146678")

    @commands.command()
    async def thicc(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/747536639089311875/766331199526273041/2020-10-15-17-05-29.png")
        await ctx.send("You thought it was viper or reyna, grow up real men knows its omen")

    @commands.command(aliases=["flox"])
    async def floxay(self, ctx):
        await ctx.send("blub blub")
    
    @commands.command()
    async def fox(self, ctx):
        r = requests.get("https://randomfox.ca/floof/")
        fox = r.json()
        await ctx.send(fox['image'])
        
    @commands.command()
    async def cat(self, ctx):
        r = requests.get("http://aws.random.cat/meow")
        cat = r.json()
        await ctx.send(cat['file'])
    
    @commands.command()
    async def dog(self, ctx):
        r = requests.get("https://some-random-api.ml/img/dog")
        dog = r.json()
        await ctx.send(dog['link'])
        
    
    @commands.command()
    async def shatter(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.dark_gold(),
            title = "__Shatter Lore:__",
            description = "[Click for Official Shatter Lore](https://www.youtube.com/watch?v=dQw4w9WgXcQ)\n[Click for Unofficial Shatter Lore](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"
        )
        embed.add_field(name = "__Agent Info:__", value="```Name: Shatter\nCodename: Shatter\nAgent ID: 1\nCountry: Unknown\nType: Controller```", inline=True)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/784077729082376192/791272831543148585/TX_Hud_Character_Shatter.png")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Egg(bot))
    print('Eastereggs.py loaded')
