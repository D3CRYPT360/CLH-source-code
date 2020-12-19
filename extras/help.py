import discord
from discord.ext import commands
from disputils import BotEmbedPaginator
import asyncio

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.version = "11.0"

    @commands.command()
    async def help(self, ctx):
        contents = [
        discord.Embed(
            title="📖 Lore Commands",
            colour=0xFF4654
        ).add_field(
            name="`/(Agent Name)`",
            value="Shows the lore about the agent specified (eg. `/cypher`)",
            inline=False
        ).add_field(
            name="`/(Map Name)`",
            value="Shows the lore about the map specified (eg. `/split`)" ,
            inline=False
        
        ).add_field(
            name="`/card (Agent Name)`",
            value="Shows the card of the specified agent (eg, `/card reyna`)",
            inline=False
        ).add_field(
            name="`/beta (Beta Agent Name)`",
            value="Shows the beta card of the specified agent (eg. `/beta omen`)",
            inline=False
        ).add_field(
            name="`/rift`",
            value="Shows Rift lore",
            inline=False
        ).set_thumbnail(
            url="https://media.discordapp.net/attachments/784077729082376192/789547598708342824/9d86482f1f4d6b19263e4aa1ea3142d8-removebg-preview.png"
        ),

        discord.Embed(
            title="✅ Useful Commands",
            description="\n`/ping`: Pong!\n\n`/stats`: Shows bot's stats\n\n`/codes`: Shows the codenames of the maps\n\n`/firstlight`: Information about the First Light event\n\n`/duelists`: Information about the Duelists cinematic\n\n`/status (Server)`: Shows the status of the specified server\n\n`/agents`: The numbers of agents in VALORANT\n\n`/languages`: The languages you can play VALORANT in",
            colour=0xFF4654
        ).set_thumbnail(
            url="https://media.discordapp.net/attachments/784077729082376192/789547598708342824/9d86482f1f4d6b19263e4aa1ea3142d8-removebg-preview.png"
        ),

        discord.Embed(
            title="🎉 Misc Commands",
            description="\n`/nitro`: Free Nitro!\n\n`/cat`: Cat pics\n\n`/dog`: Dog pics\n\n`/fox`: Fox pics",
            colour=0xFF4654
        ).set_thumbnail(
            url="https://media.discordapp.net/attachments/784077729082376192/789547598708342824/9d86482f1f4d6b19263e4aa1ea3142d8-removebg-preview.png"
        )
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

    @commands.command()
    async def stats(self, ctx):
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        memberCount = len(set(self.bot.get_all_members()))

        embed = discord.Embed(title=f'{self.bot.user.name} Stats', description='', colour=discord.Colour.red(), timestamp=ctx.message.created_at)

        embed.add_field(name='Bot Version:', value=self.bot.version)
        embed.add_field(name='Python Version:', value=pythonVersion)
        embed.add_field(name='Discord.py Version', value=dpyVersion)
        embed.add_field(name='C.V. Lore Den Members:', value=memberCount)
        embed.add_field(name='Bot Developers:', value="<@482179909633048597>\n<@563361513281421313>")


        embed.set_footer(text=f"{self.bot.user.name}")
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/784077729082376192/789547598708342824/9d86482f1f4d6b19263e4aa1ea3142d8-removebg-preview.png")

        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')


def setup(bot):
    bot.add_cog(Help(bot))
    print('Help.py loaded')
