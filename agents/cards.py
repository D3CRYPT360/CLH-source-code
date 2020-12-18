import discord
from discord.ext import commands

class __Cards__(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(hidden=True)
    async def card(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("`/card (agent name)`")

    @commands.command(description='shows the usage of card commands')
    async def helpcard(self, ctx):
        await ctx.send('`/card (agent name)`')

    #brimstone Card#
    @card.command(aliases = ['brim', 'sarge'], description="Shows Brimstone's card")
    async def brimstone(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blurple(),
            title='No One Left Behind Card'
        )

        embed.set_image(url="https://cdn.discordapp.com/attachments/748151130797899858/750324551283638312/Brimstone_Half_2.png")

        await ctx.send(embed=embed)

    #viper card#
    @card.command(aliases = ['pandemic' , 'sabine'], description="Shows Viper's card")
    async def viper(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blurple(),
            title='One Dark Night Card'
        )

        embed.set_image(url="https://cdn.discordapp.com/attachments/748151130797899858/750324627292815360/Viper_home.png")

        await ctx.send(embed=embed)

    #omencard#
    @card.command(aliases = ['wraith'], description="Shows Omen's Card")
    async def omen(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blurple(),
            title='Whats Another Death Card'
        )

        embed.set_image(url="https://cdn.discordapp.com/attachments/748151130797899858/750324587388076171/omen_home_1.png")

        await ctx.send(embed=embed)

     #killjoy card#
    @card.command(aliases = ['kj'], description="Shows Killjoy's card")
    async def killjoy(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blurple(),
            title='Nachtelang Card'
        )

        embed.set_image(url="https://cdn.discordapp.com/attachments/748151130797899858/750324710608339035/Killjoy_life_event.png")

        await ctx.send(embed=embed)

    #Cypher card#
    @card.command(aliases = ['aamir' , 'gumshoe'], description="Shows Cypher's card")
    async def cypher(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blurple(),
            title='Redeemers Folly'
        )

        embed.set_image(url="https://cdn.discordapp.com/attachments/748151130797899858/750328801312899132/Cypher_home_2.png")

        await ctx.send(embed=embed)

    #Sova Card#
    @card.command(aliases = ['hunter', 'constant', 'constantvalorant'], description="Shows Sova's card")
    async def sova(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blurple(),
            title='Through The Looking Glass'
        )
        embed.set_author(name='Constant Lore Helper', icon_url= 'https://cdn.discordapp.com/attachments/746555773206790288/750921999119024168/CLHpfp.png')
        embed.set_image(url="https://cdn.discordapp.com/attachments/748151130797899858/750324618698686584/Sova_home_1.png")

        await ctx.send(embed=embed)

    #Sage Card#
    @card.command(aliases = ['thorne'], description="Shows Sage's card")
    async def sage(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blurple(),
            title='Journey Of Trials Card'
        )

        embed.set_image(url="https://cdn.discordapp.com/attachments/748151130797899858/750324655205777416/Sage_home_1.png")

        await ctx.send(embed=embed)

    #Phoenix Card#
    @card.command(aliases = ['grant' , 'phx'], description="Shows Phoenix's card")
    async def phoenix(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blurple(),
            title='Firestarter Card'
        )

        embed.set_image(url="https://cdn.discordapp.com/attachments/748151130797899858/750324604496511016/Phoenix_House_burn_1.png")

        await ctx.send(embed=embed)

    #Jett Card#
    @card.command(aliases = ['wushu'], description="Shows Jett's card")
    async def jett(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blurple(),
            title='Mirrored Edge Card'
        )

        embed.set_image(url="https://cdn.discordapp.com/attachments/748151130797899858/750324570522648686/Jett_home_2.png")

        await ctx.send(embed=embed)

    #Reyna Card#
    @card.command(aliases = ['vampire'], description="Shows the Reyna's card")
    async def reyna(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blurple(),
            title='Revenge For Life Card'
        )

        embed.set_image(url="https://media.discordapp.net/attachments/748151130797899858/750324666798702592/Reyna_Desert_1.png?width=209&height=499")

        await ctx.send(embed=embed)

    #Raze Card#
    @card.command(aliases = ['clay'], description="Shows Raze's card")
    async def raze(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blurple(),
            title='Rising Up Card'
        )

        embed.set_image(url="https://media.discordapp.net/attachments/748151130797899858/750324969195569152/Raze_home_1.png?width=209&height=499")

        await ctx.send(embed=embed)


    #Breach Card#
    @card.command(aliases = ['cabbage' , 'lettuce'], description="Shows breach's card")
    async def breach(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blurple(),
            title='Big Payday Card'
        )

        embed.set_image(url="https://images-ext-1.discordapp.net/external/r1T046SjilYgHTu4DN83a6NFOMnL1pGIUfBMK-myw4s/%3Fwidth%3D209%26height%3D499/https/media.discordapp.net/attachments/748151130797899858/750324506391740426/Breach_Bank_1.png")
        await ctx.send(embed=embed)
        
    #Breach Card#
    @card.command(aliases = ['aussie' , 'mate', 'upsidedown'], description="Shows breach's card")
    async def skye(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blurple(),
            title='The Great Reclaimer'
        )

        embed.set_image(url="https://cdn.discordapp.com/attachments/745696342260711516/774936054502653952/ZKcAxKS.png")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(__Cards__(bot))
    print('Cards.py loaded')
