import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import time

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(description="Gives free nitro updates everyday :D")
    async def nitro(self, ctx):
        await ctx.send('<:kekyou:761896381404938241>')


    @commands.command(aliases = ['lang'])
    async def languages(self, ctx):
        embed = discord.Embed(
            title="Languages supported by Valorant",
            color=0xFF4654,
        )
        embed.add_field(name="ENGLISH ", value="English", inline=True)
        embed.add_field(name="ESPANOL ", value="Spanish")
        embed.add_field(name="FRANÇAIS", value="French")
        embed.add_field(name="ITALIANO ", value="Italian")
        embed.add_field(name="POLSKI ", value="Polish")
        embed.add_field(name="Русский ", value="Russian")
        embed.add_field(name="日本語 ", value="Japanese ")
        embed.add_field(name="한국어 ", value="Korean")
        embed.add_field(name="繁體中文 ", value="Chinese")
        embed.add_field(name="Português ", value="portugese")
        embed.add_field(name="Tiếng Việt ", value=" Vietnamese")
        embed.add_field(name="DEUTSCH ", value="German")
        embed.add_field(name="TÜRKÇE", value="Turkish")
        embed.add_field(name="العربية", value="Arabic")
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 765992140115017758:
            await message.add_reaction("<:upvote:762456415751110697>")

def setup(bot):
    bot.add_cog(Misc(bot))
    print('Misc.py loaded')
