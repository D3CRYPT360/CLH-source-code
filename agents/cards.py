import discord
from discord.ext import commands
import DiscordUtils
from utils.requesting import Agents, Card
from utils.card_def import card_coverter_global, card_coverter_beta
from utils.agent_def import agent_hex

class Cards(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def card(self, ctx, card):
        json_data = Card()
        card = card.capitalize()
        card_name = card_coverter_global(card)
        for i in range(len(json_data['data'])):
            if json_data['data'][i]['displayName'] == card_name:
                embed = discord.Embed(
                    colour = agent_hex(card),
                    title='{}'.format(card_name)
                )
                embed.set_image(url="{}".format(json_data['data'][i]['largeArt']))
                await ctx.send(embed=embed)

    @commands.command()
    async def beta(self, ctx, beta_card):
        json_data = Agents()
        beta_card = beta_card.capitalize()
        try:
            
            if beta_card == "Raze":
                embed = discord.Embed(
                    colour = agent_hex(beta_card),
                )
                embed.set_image(url="{}".format(card_coverter_beta("Raze")))
                await ctx.send(embed=embed)
            else: 
                for i in range(len(json_data['data'])):
                    if json_data['data'][i]['displayName'] == beta_card:
                        embed1 = discord.Embed(
                            colour = agent_hex(beta_card),
                        )
                        embed1.set_image(url="{}".format(card_coverter_beta(beta_card)[0]))
                        
                        embed2 = discord.Embed(
                            colour = agent_hex(beta_card),
                        )
                        embed2.set_image(url="{}".format(card_coverter_beta(beta_card)[1]))
                        
                        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, auto_footer = True)
                        paginator.add_reaction('⬅️', "back")
                        paginator.add_reaction('➡️', "next")
                        embeds = [embed1, embed2]
                        await paginator.run(embeds)
        except TypeError:
            await ctx.send(f"{beta_card} was not an Agent in the closed Beta. Try again with an agent who was in the closed beta", delete_after=5)

def setup(bot):
    bot.add_cog(Cards(bot))
    print('Cards.py loaded')
