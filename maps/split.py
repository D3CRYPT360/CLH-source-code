import discord
from discord.ext import commands

class split(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    @commands.group(aliases=["bonsai"])
    async def split(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
            colour=discord.Colour.teal(),
            title = "Unoffical split Lore:\nhttps://discordapp.com/channels/708983243847761931/747040395891966002/747051202482667602\nScrapped Split Lore:\nhttps://discordapp.com/channels/708983243847761931/749305721467699273/749902333302800384"
            )
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/747040395891966002/747051800779161680/brian-yam-ares-env-bonsai-train-redesign02c_r.jpg")
            embed.add_field(name="__split info__", value="```\n-Code name = Bonsai\n-Location =  Tokyo Japan\n-Coordinates = 35.683333, 139.683333```")
            embed.set_footer(text= "use `/split un` to see the unconfirmed lore")
            await ctx.send(embed=embed)


    @split.command(aliases=["unconfirmed"])
    async def un(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.teal(),
            title = "Unconfirmed Split lore:\nhttps://discordapp.com/channels/708983243847761931/749187232530825266/749326681923256340"
        )
        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(split(bot))
    print('split is loaded')
