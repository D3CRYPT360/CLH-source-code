import discord
from discord.ext import commands
import asyncio

class maps(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=["bonsai"])
    async def split(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.teal(),
            title = "__Split Lore:__",
            description="[Click for General Lore](https://discordapp.com/channels/708983243847761931/747040395891966002/747051202482667602)\n[Click for Unconfirmed Lore](https://discordapp.com/channels/708983243847761931/749187232530825266/749326681923256340)\n[Click for Scrapped Lore](https://discordapp.com/channels/708983243847761931/749305721467699273/749902333302800384)",
        )
        embed.set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486400960856094/Bonsai_preview.png"),
        embed.add_field(name="__Split Info:__", value="```\nCodename: Bonsai\nLocation: Tokyo/Japan\nCoordinates: 35.683333, 139.683333```"),
        await ctx.send(embed=embed)


    @commands.command(aliases=["duality"])
    async def bind(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_gold(),
            title = "__Bind Lore:__",
            description="[Click for General Lore](https://discord.com/channels/708983243847761931/747040395891966002/747143027440484453)\n[Click for Unconfirmed Lore](https://discord.com/channels/708983243847761931/749187232530825266/749309432994726011)\n[Click for Scrapped Lore](https://discord.com/channels/708983243847761931/749305721467699273/749898301335142411)",
        )
        embed.set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486406762233946/Duality_preview.png"),
        embed.add_field(name="__Bind Info:__", value="```\nCodename: Duality\nLocation: Rabat/Morocco\nCoordinates: 34.033333, -6.850000```"),
        await ctx.send(embed=embed)
    
    
    @commands.command(aliases=["triad"])
    async def haven(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.red(),
            title = "__Haven Lore:__",
            description="[Click for General Lore](https://discord.com/channels/708983243847761931/747040395891966002/747392315944992819)\n[Click for Scrapped Lore](https://discord.com/channels/708983243847761931/749305721467699273/749914184367472713)",
        )
        embed.set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486415570272266/Triad_preview.png"),
        embed.add_field(name="__Haven Info:__", value="```\nCodename: Triad\nLocation: Thimphu/Bhutan\nCoordinates: 27.466667, 89.633333```"),
        await ctx.send(embed=embed)


    @commands.command(aliases=["venice"])
    async def ascent(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_orange(),
            title = "__Ascent Lore:__",
            description="[Click for General Lore](https://discord.com/channels/708983243847761931/747040395891966002/747136697036177458)\n[Click for Unconfirmed Lore](https://discord.com/channels/708983243847761931/749187232530825266/749306607669608499)\n[Click for Scrapped Lore](https://discord.com/channels/708983243847761931/749305721467699273/749914435455549480)",
        )
        embed.set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486398855053312/Ascent_preview.png"),
        embed.add_field(name="__Ascent Info:__", value="```\nCodename: Venice\nLocation: Venice/Italy\nCoordinates: 45.433333, 12.333333```"),
        await ctx.send(embed=embed)


    @commands.command(aliases=["port"])
    async def icebox(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blurple(),
            title = "__Icebox Lore:__",
            description="[Click for General Lore](https://discord.com/channels/708983243847761931/747040395891966002/763054857421848597)\n[Click for Unconfirmed Lore](https://discord.com/channels/708983243847761931/749187232530825266/763068019030229022)\n[Click for Scrapped Lore](https://discord.com/channels/708983243847761931/749305721467699273/763323710764613632)",
        )
        embed.set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486419868385310/Icebox_preview.png"),
        embed.add_field(name="__Icebox Info:__", value="```\nCodename: Port\nLocation: Bennett Island/Russia\nCoordinates: 76.733333, 149.500000```"),
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(maps(bot))
    print('Maps.py loaded')