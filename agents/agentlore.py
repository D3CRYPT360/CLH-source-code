import discord
import asyncio
from discord.ext import commands
from utils.agent_def import agent_country, real_name, agent_order, lore_link_official, lore_link_unofficial, agent_hex
from utils.requesting import Agents

class AgentLore(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def agent(self, ctx, agent):
        json_data = Agents()
        agent = agent.capitalize()
        for i in range(len(json_data['data'])):
            if json_data['data'][i]['displayName'] == agent:
                contents = [
                discord.Embed(
                    colour = agent_hex(agent),
                    title = "__{} Lore:__".format(json_data['data'][i]['displayName']),
                    description = "[Click for Official {} Lore]({})".format(json_data['data'][i]['displayName'], lore_link_official(agent)) + "\n[Click for Unofficial {} Lore]({})".format(json_data['data'][i]['displayName'], lore_link_unofficial(agent))
                ).add_field(name = "__Agent Info:__",value="```Name: {}\nCodename: {}\nReal Name: {}\nAgent ID: {}\nCountry: {}\nType: {}```".format(json_data['data'][i]['displayName'],json_data['data'][i]['developerName'],real_name(agent), agent_order(agent),agent_country(agent),json_data['data'][i]['role']['displayName']),inline=True).set_thumbnail(url="{}".format(json_data['data'][i]['displayIcon'])).set_footer(text="Page 1/4"),
                
                discord.Embed(
                    colour = agent_hex(agent),
                    title = "__{}__".format(json_data['data'][i]['abilities'][1]['displayName'])
                ).add_field(name = "_ _", value = "```{}```".format(json_data['data'][i]['abilities'][1]['description'])).set_thumbnail(url="{}".format(json_data['data'][i]['abilities'][1]['displayIcon'])).set_footer(text="Page 2/4"),
                
                discord.Embed(
                    colour = agent_hex(agent),
                    title = "__{}__".format(json_data['data'][i]['abilities'][2]['displayName'])
                ).add_field(name = "_ _",value = "```{}```".format(json_data['data'][i]['abilities'][2]['description'])).set_thumbnail(url="{}".format(json_data['data'][i]['abilities'][2]['displayIcon'])).set_footer(text="Page 3/4"),
                
                discord.Embed(
                    colour = agent_hex(agent),
                    title = "__{}__".format(json_data['data'][i]['abilities'][3]['displayName'])
                ).add_field(name = "_ _", value = "```{}```".format(json_data['data'][i]['abilities'][3]['description'])).set_thumbnail(url="{}".format(json_data['data'][i]['abilities'][3]['displayIcon'])).set_footer(text="Page 4/4"),
                ]
                pages = 4
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
                                 

    @commands.command(aliases = ['brimstone','omen','killjoy', 'cypher', 'sage' ,'sova', 'phoneix', 'jett', 'skye', 'reyna', 'raze', 'breach'])
    async def viper(self, ctx):
        await ctx.send("Command has changed to `/agent [agentname]` without the []", delete_after=5)

    @commands.command(description="Shows the lore about rifts")
    async def rift(self, ctx):
        embed = discord.Embed(
            colour=0x48ADEB,
            title="**Rift Lore**:",
            description="[Click for Rift lore](https://discord.com/channels/708983243847761931/727811131254505523/748854274343043152)",
        )
        embed.add_field(name="__Rift Info__", value="```A Rift is a wormhole (found in the game files).\n\nA wormhole can be visualized as a tunnel with two ends at seperate points in spacetime (i.e., different locations or different points in time, or both).```")
        embed.set_image(url="https://cdn.discordapp.com/attachments/784077729082376192/789785522016747542/skye__agent_reveal_trailer_-_v_1.gif")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AgentLore(bot))
    print('Agentlore.py loaded')
