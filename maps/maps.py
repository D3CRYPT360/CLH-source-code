import discord
from discord.ext import commands
import asyncio

class maps(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=["bonsai"])
    async def split(self, ctx):
        contents = [
        discord.Embed(
            colour=discord.Colour.teal(),
            title = "General Split Lore:",
            description="[Click for General Lore](https://discordapp.com/channels/708983243847761931/747040395891966002/747051202482667602)",
        ).set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486400960856094/Bonsai_preview.png").add_field(name="__Split Info__", value="```\nCodename: Bonsai\nLocation: Tokyo/Japan\nCoordinates: 35.683333, 139.683333```"),

        discord.Embed(
            colour=discord.Colour.teal(),
            title = "Unconfirmed Split lore:",
            description="[Click for Unconfirmed Lore](https://discordapp.com/channels/708983243847761931/749187232530825266/749326681923256340)",
        ).set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486400960856094/Bonsai_preview.png").add_field(name="__Split Info__", value="```\nCodename: Bonsai\nLocation: Tokyo/Japan\nCoordinates: 35.683333, 139.683333```"),

        discord.Embed(
            colour=discord.Colour.teal(),
            title="Scrapped Split Lore:",
            description="[Click for Scrapped Lore](https://discordapp.com/channels/708983243847761931/749305721467699273/749902333302800384)",
        ).set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486400960856094/Bonsai_preview.png").add_field(name="__Split Info__", value="```\nCodename: Bonsai\nLocation: Tokyo/Japan\nCoordinates: 35.683333, 139.683333```")

        ]
        
        pages = 3
        cur_page = 1
        message = await ctx.send(embed=contents[cur_page-1])

        await message.add_reaction("◀️")
        await message.add_reaction("▶️")
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=180, check=check)

                if str(reaction.emoji) == "▶️" and cur_page != pages:
                    cur_page += 1
                    await message.edit(embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "◀️" and cur_page > 1:
                    cur_page -= 1
                    await message.edit(embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

                else:
                    await message.remove_reaction(reaction, user)

            except asyncio.TimeoutError:
                break

    @commands.command(aliases=["duality"])
    async def bind(self, ctx):
        contents = [
        discord.Embed(
            colour=discord.Colour.dark_gold(),
            title = "General Bind Lore:",
            description="[Click for General Lore](https://discord.com/channels/708983243847761931/747040395891966002/747143027440484453)",
        ).set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486406762233946/Duality_preview.png").add_field(name="__Bind Info__", value="```\nCodename: Duality\nLocation: Rabat/Morocco\nCoordinates: 34.033333, -6.850000```"),

        discord.Embed(
            colour=discord.Colour.dark_gold(),
            title = "Unconfirmed Bind lore:",
            description="[Click for Unconfirmed Lore](https://discord.com/channels/708983243847761931/749187232530825266/749309432994726011)",
        ).set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486406762233946/Duality_preview.png").add_field(name="__Bind Info__", value="```\nCodename: Duality\nLocation: Rabat/Morocco\nCoordinates: 34.033333, -6.850000```"),

        discord.Embed(
            colour=discord.Colour.dark_gold(),
            title="Scrapped Bind Lore:",
            description="[Click for Scrapped Lore](https://discord.com/channels/708983243847761931/749305721467699273/749898301335142411)",
        ).set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486406762233946/Duality_preview.png").add_field(name="__Bind Info__", value="```\nCodename: Duality\nLocation: Rabat/Morocco\nCoordinates: 34.033333, -6.850000```")

        ]
        
        pages = 3
        cur_page = 1
        message = await ctx.send(embed=contents[cur_page-1])

        await message.add_reaction("◀️")
        await message.add_reaction("▶️")
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=180, check=check)

                if str(reaction.emoji) == "▶️" and cur_page != pages:
                    cur_page += 1
                    await message.edit(embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "◀️" and cur_page > 1:
                    cur_page -= 1
                    await message.edit(embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

                else:
                    await message.remove_reaction(reaction, user)

            except asyncio.TimeoutError:
                break
    
    @commands.command(aliases=["triad"])
    async def haven(self, ctx):
        contents = [
        discord.Embed(
            colour=discord.Colour.red(),
            title = "General Haven Lore:",
            description="[Click for General Lore](https://discord.com/channels/708983243847761931/747040395891966002/747392315944992819)",
        ).set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486415570272266/Triad_preview.png").add_field(name="__Haven Info__", value="```\nCodename: Triad\nLocation: Thimphu/Bhutan\nCoordinates: 27.466667, 89.633333```"),

        discord.Embed(
            colour=discord.Colour.red(),
            title="Scrapped Haven Lore:",
            description="[Click for Scrapped Lore](https://discord.com/channels/708983243847761931/749305721467699273/749914184367472713)",
        ).set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486415570272266/Triad_preview.png").add_field(name="__Haven Info__", value="```\nCodename: Triad\nLocation: Thimphu/Bhutan\nCoordinates: 27.466667, 89.633333```")

        ]
        
        pages = 2
        cur_page = 1
        message = await ctx.send(embed=contents[cur_page-1])

        await message.add_reaction("◀️")
        await message.add_reaction("▶️")
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=180, check=check)

                if str(reaction.emoji) == "▶️" and cur_page != pages:
                    cur_page += 1
                    await message.edit(embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "◀️" and cur_page > 1:
                    cur_page -= 1
                    await message.edit(embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

                else:
                    await message.remove_reaction(reaction, user)

            except asyncio.TimeoutError:
                break

    @commands.command(aliases=["venice"])
    async def ascent(self, ctx):
        contents = [
        discord.Embed(
            colour=discord.Colour.dark_orange(),
            title = "General Ascent Lore:",
            description="[Click for General Lore](https://discord.com/channels/708983243847761931/747040395891966002/747136697036177458)",
        ).set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486398855053312/Ascent_preview.png").add_field(name="__Ascent Info__", value="```\nCodename: Venice\nLocation: Venice/Italy\nCoordinates: 45.433333, 12.333333```"),

        discord.Embed(
            colour=discord.Colour.dark_orange(),
            title = "Unconfirmed Ascent lore:",
            description="[Click for Unconfirmed Lore](https://discord.com/channels/708983243847761931/749187232530825266/749306607669608499)",
        ).set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486398855053312/Ascent_preview.png").add_field(name="__Ascent Info__", value="```\nCodename: Venice\nLocation: Venice/Italy\nCoordinates: 45.433333, 12.333333```"),

        discord.Embed(
            colour=discord.Colour.dark_orange(),
            title="Scrapped Ascent Lore:",
            description="[Click for Scrapped Lore](https://discord.com/channels/708983243847761931/749305721467699273/749914435455549480)",
        ).set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486398855053312/Ascent_preview.png").add_field(name="__Ascent Info__", value="```\nCodename: Venice\nLocation: Venice/Italy\nCoordinates: 45.433333, 12.333333```")

        ]
        
        pages = 3
        cur_page = 1
        message = await ctx.send(embed=contents[cur_page-1])

        await message.add_reaction("◀️")
        await message.add_reaction("▶️")
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=180, check=check)

                if str(reaction.emoji) == "▶️" and cur_page != pages:
                    cur_page += 1
                    await message.edit(embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "◀️" and cur_page > 1:
                    cur_page -= 1
                    await message.edit(embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

                else:
                    await message.remove_reaction(reaction, user)

            except asyncio.TimeoutError:
                break

    @commands.command(aliases=["port"])
    async def icebox(self, ctx):
        contents = [
        discord.Embed(
            colour=discord.Colour.blurple(),
            title = "General Icebox Lore:",
            description="[Click for General Lore](https://discord.com/channels/708983243847761931/747040395891966002/763054857421848597)",
        ).set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486419868385310/Icebox_preview.png").add_field(name="__Icebox Info__", value="```\nCodename: Port\nLocation: Bennett Island/Russia\nCoordinates: 76.733333, 149.500000```"),
        
        discord.Embed(
            colour=discord.Colour.blurple(),
            title = "Unconfirmed Icebox lore:",
            description="[Click for Unconfirmed Lore](https://discord.com/channels/708983243847761931/749187232530825266/763068019030229022)",
        ).set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486419868385310/Icebox_preview.png").add_field(name="__Icebox Info__", value="```\nCodename: Port\nLocation: Bennett Island/Russia\nCoordinates: 76.733333, 149.500000```"),

        discord.Embed(
            colour=discord.Colour.blurple(),
            title="Scrapped Icebox Lore:",
            description="[Click for Scrapped Lore](https://discord.com/channels/708983243847761931/749305721467699273/763323710764613632)",
        ).set_image(url="https://media.discordapp.net/attachments/784077729082376192/789486419868385310/Icebox_preview.png").add_field(name="__Icebox Info__", value="```\nCodename: Port\nLocation: Bennett Island/Russia\nCoordinates: 76.733333, 149.500000```")

        ]
        
        pages = 3
        cur_page = 1
        message = await ctx.send(embed=contents[cur_page-1])

        await message.add_reaction("◀️")
        await message.add_reaction("▶️")
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=180, check=check)

                if str(reaction.emoji) == "▶️" and cur_page != pages:
                    cur_page += 1
                    await message.edit(embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "◀️" and cur_page > 1:
                    cur_page -= 1
                    await message.edit(embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

                else:
                    await message.remove_reaction(reaction, user)

            except asyncio.TimeoutError:
                break

def setup(bot):
    bot.add_cog(maps(bot))
    print('Maps.py loaded')