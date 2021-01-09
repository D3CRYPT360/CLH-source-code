import discord
from discord.ext import commands
from datetime import datetime
import string
import random

def gen_key():
    alpha, num = list(string.ascii_lowercase), list(string.digits)
    mapper = []
    for i in range(10):
        x = ('y', 'n')
        if random.choice(x) == 'y':
            if random.choice(x) == 'y':
                mapper.append(random.choice(alpha).upper())
            else:
                mapper.append(random.choice(alpha))
        else:
            mapper.append(str(random.choice(num)))
    return ''.join(map(str, mapper))


class Suggestions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sid_keys = {}

    @commands.command()
    async def suggest(self, ctx, *, suggestion):
        #channel1=self.bot.get_channel(747516232093270088)
        channel2=self.bot.get_channel(747525554491752480)

        embed = discord.Embed(title=" ", description=" ", colour=ctx.author.colour, timestamp=ctx.message.created_at)
        embed.add_field(name="Submitted by:", value=ctx.author, inline=False)
        embed.add_field(name="Suggestion:", value=suggestion, inline=False)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        suggestion_message = await channel2.send(embed=embed)
        sid = gen_key()
        embed.set_footer(text="SID: {}".format(sid))
        self.sid_keys[sid] = suggestion_message.id
        await suggestion_message.edit(embed=embed)

    @commands.command()
    async def reject(self, ctx, suggest : str=None):
        if id == None:
            embed = suggestion_message.embeds[0]
            return await ctx.send("Please Enter SID", delete_after=5)
        suggestion_message = await ctx.channel.fetch_message(self.sid_keys[suggest])
        if not suggestion_message:
            return await ctx.send("Please Enter a valid ID!!")
        

    @commands.command()
    async def tally(self, ctx, poll : str=None):
        if id == None:
            return await ctx.send("Please Enter poll ID")
        poll_message = await ctx.channel.fetch_message(self.poll_keys[poll])
        if not poll_message:
            return await ctx.send('Please enter the correct id!')
        embed = poll_message.embeds[0]
        unformatted_options = [x.strip() for x in embed.description.split('\n')]
        print(f'unformatted{unformatted_options}')
        opt_dict = {x[:2]: x[3:] for x in unformatted_options} if unformatted_options[0][0] == '1' \
            else {x[:1]: x[2:] for x in unformatted_options}
        # check if we're using numbers for the poll, or x/checkmark, parse accordingly
        voters = [self.bot.user.id]  # add the bot's ID to the list of voters to exclude it's votes

        tally = {x: 0 for x in opt_dict.keys()}
        for reactions in poll_message.reactions:
            if reactions.emoji in opt_dict.keys():
                reactors = await reactions.users().flatten()
                for reactor in reactors:
                    if reactor.id not in voters:
                        tally[reactions.emoji] += 1
                        voters.append(reactor.id)
        output = f"Results of the poll for **{embed.title}**:\n" + '\n'.join(['{}: {}'.format(opt_dict[key], tally[key]) for key in tally.keys()])
        await ctx.send(output)
        await poll_message.clear_reactions()

def setup(bot):
    bot.add_cog(Suggestions(bot))
    print("Suggestions.py loaded")