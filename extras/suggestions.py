import discord
from discord.ext import commands
from datetime import datetime
import string
import random
import uuid

id = uuid.uuid1()

class Suggestions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def suggest(self, ctx, *, suggestion):
        #channel1=self.bot.get_channel(747516232093270088)
        channel2=self.bot.get_channel(747525554491752480)

        embed = discord.Embed(title=" ", description=" ", colour=ctx.author.colour, timestamp=ctx.message.created_at)
        embed.add_field(name="Submitted by:", value=ctx.author, inline=False)
        embed.add_field(name="Suggestion:", value=suggestion, inline=False)
        embed.set_footer(text="Suggestion ID: "+str(id))
        embed.set_thumbnail(url=ctx.author.avatar_url)
        #await channel1.send(embed=embed)
        await channel2.send(embed=embed)

def setup(bot):
    bot.add_cog(Suggestions(bot))
    print('Suggestions.py loaded')