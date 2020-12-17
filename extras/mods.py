import discord
from discord.ext.commands import has_permissions


class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=["r"], hidden=True)
    @has_permissions(kick_members=True)
    async def rule(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("/r [rule number or keyword in rule]\n/r tags <- [to see all the tags]")


    @rule.command(aliases=["1", "harrasment", "discrimination", "race"])
    @has_permissions(kick_members=True)
    async def _1(self, ctx):
        embed = discord.embed(title=":zero::one: No hate speech, harassment or discrimination:", description="Discrimination against race, sex, orientation, etc. and using slurs of any kind.", colour=0x00FF8B)
        embed.set_footer(text="Punishment: -> Ban")
        await ctx.send(embed=embed)

    @rule.command(aliases=["2", "english", "nonenglish"])
    @has_permissions(kick_members=True)
    async def _2(self, ctx):
        embed = discord.embed(title=":zero::two: English only:", description="This excludes talking about the lore that is in other languages and using the <#727952098724937770> channel for talking in other languages.", colour=0x00FF8B)
        embed.set_footer(text="Punishment: Warn -> 1 Strike")
        await ctx.send(embed=embed)

    @rule.command(aliases=["3", "nsfw"])
    @has_permissions(kick_members=True)
    async def _3(self, ctx):
        embed = discord.embed(title=":zero::three: No NSFW content:", description="No NSFW content anywhere on the server, (NSFW chats, messages, drawings, gifs etc...)", colour=0x00FF8B)
        embed.set_footer(text="Punishment: -> Ban")
        await ctx.send(embed=embed)

    @rule.command(aliases=["4", "pfp", "profile", "username", "nickname", "status"])
    @has_permissions(kick_members=True)
    async def _4(self, ctx):
        embed = discord.embed(title=":zero::four: Use appropriate profile pictures, usernames and statuses:", description="Make sure your username/nickname is pingable if not mods have the rights to change it, user PFP shouldn't break any other server rules such as no NSFW or self promo rules.", colour=0x00FF8B)
        embed.set_footer(text="Punishment: Warn -> Ban")
        await ctx.send(embed=embed)

    @rule.command(aliases=["5", "impersonation", "imp"])
    @has_permissions(kick_members=True)
    async def _5(self, ctx):
        embed = discord.embed(title=":zero::five: No impersonation of mods, riot staff or other users:", description="Impersonating someone by changing your username or PFP to match theirs is strictly forbidden.", colour=0x00FF8B)
        embed.set_footer(text="Punishment: Warn -> Mute")
        await ctx.send(embed=embed)

    @rule.command(aliases=["6", "religion", "politics", "controversial"])
    @has_permissions(kick_members=True)
    async def _6(self, ctx):
        embed = discord.embed(title=":zero::six: No politics, religion, or other controversial topics:", description="This excludes any politics and religions in the Valorant lore universe.", colour=0x00FF8B)
        embed.set_footer(text="Punishment: -> 2 Strikes")
        await ctx.send(embed=embed)

    @rule.command(aliases=["7", "spam", "emojispam", "links", "mention"])
    @has_permissions(kick_members=True)
    async def _7(self, ctx):
        embed = discord.embed(title=":zero::seven: No spam:", description="This includes (but not limited to) links, emojis, mentions, images, and text except in <#758010028119556217> (excluding mentions). Bot spam is allowed in bot channels.", colour=0x00FF8B)
        embed.set_footer(text="Punishment: Warn -> 1 Strike")
        await ctx.send(embed=embed)

    @rule.command(aliases=["8", "topic"])
    @has_permissions(kick_members=True)
    async def _8(self, ctx):
        embed = discord.embed(title=":zero::eight: Stay on the channel topic:", description="We may ask you to switch channels if you go off-topic. Please refer to the channel topics if you are confused about what a channel is for.", colour=0x00FF8B)
        embed.set_footer(text="Punishment: Warn -> 1 Strike")
        await ctx.send(embed=embed)
        
    @rule.command(aliases=["9", "dox", "doxxing", "doxx", "personal"])
    @has_permissions(kick_members=True)
    async def _9(self, ctx):
        embed = discord.embed(title=":zero::nine: No doxing or discussing another user's personal information:", description="This includes information such as name, address, other account names, etc. Joking about this information is also not allowed.", colour=0x00FF8B)
        embed.set_footer(text="Punishment: -> Ban")
        await ctx.send(embed=embed)

    @rule.command(aliases=["10", "bug", "bugs", "exploit", "exploitation"])
    @has_permissions(kick_members=True)
    async def _10(self, ctx):
        embed = discord.embed(title=":one::zero: No exploiting server bugs:", description="If there is a bug with a channel, role, or bot trying to exploit it is not allowed. If you find a bug, please report it to us via <@748090200273584188>.", colour=0x00FF8B)
        embed.set_footer(text="Punishment: -> Ban")
        await ctx.send(embed=embed)

    @rule.command(aliases=["11", "riot", "dev", "devs", "riotping", "devping"])
    @has_permissions(kick_members=True)
    async def _11(self, ctx):
        embed = discord.embed(title=":one::one: Do not ping Riot Devs:", description="Riot staff are usually busy with their work and having them in our server is a privilege; please do not disturb them if they want to talk let them participate.", colour=0x00FF8B)
        embed.set_footer(text="Punishment: -> Warn -> 3 Strikes")
        await ctx.send(embed=embed)

    @rule.command(aliases=["12", "promo", "selfpromo", "invites"])
    @has_permissions(kick_members=True)
    async def _12(self, ctx):
        embed = discord.embed(title=":one::two: Self-promotion:", description="You can promote your (but not limited to) YouTube channel/stream, twitch channel/stream in <#776484527597551627>. However posting links to servers or harmful websites/links is not acceptable.", colour=0x00FF8B)
        embed.set_footer(text="Punishment: -> 3 Strikes")
        await ctx.send(embed=embed)
    
    @rule.command(aliases=["13", "cheats", "begging", "buying", "selling"])
    @has_permissions(kick_members=True)
    async def _13(self, ctx):
        embed = discord.embed(title=":one::three: Discussing cheats and other bannable actions:", description="Such as (but not limited to) buying, selling, trading, giving away, or begging for accounts, cheats,\"boosting\", VP, codes, money, referrals, or other goods.", colour=0x00FF8B)
        embed.set_footer(text="Punishment: Warn -> Ban")
        await ctx.send(embed=embed)
        
    @rule.command(aliases=["14", "guidelines", "tos"])
    @commands.guild_has_permissions(ban_members=True)
    async def _14(self, ctx):
        embed = discord.embed(title=":one::three: Discussing cheats and other bannable actions:", description="Such as (but not limited to) buying, selling, trading, giving away, or begging for accounts, cheats,\"boosting\", VP, codes, money, referrals, or other goods.", colour=0x00FF8B)
        embed.set_footer(text="Punishment: -> Ban")
        await ctx.send(embed=embed)       

    @rule.command(aliases=["tag"])
    @has_permissions(kick_members=True)
    async def tags(self, ctx):
        embed = discord.Embed(title="Rule Tags", description="\u200b", colour=discord.Colour.red())
        embed.add_field(name="Rule 1", value="[harrasment, discrimination, race]", inline=False)
        embed.add_field(name="Rule 2", value="[english, nonenglish]", inline=False)
        embed.add_field(name="Rule 3", value="[nsfw]", inline=False)
        embed.add_field(name="Rule 4", value="[pfp, profile, username, nickname, status]", inline=False)
        embed.add_field(name="Rule 5", value="[impersonation, imp]", inline=False)
        embed.add_field(name="Rule 6", value="[religion, politics, controversial]", inline=False)
        embed.add_field(name="Rule 7", value="[spam, emojispam, links, mention]", inline=False)
        embed.add_field(name="Rule 8", value="[topic]", inline=False)
        embed.add_field(name="Rule 9", value="[dox, doxxing, doxx, personal]", inline=False)
        embed.add_field(name="Rule 10", value="[bug, bugs, exploit, exploitation]", inline=False)
        embed.add_field(name="Rule 11", value="[riot, dev, devs, riotping, devping]", inline=False)
        embed.add_field(name="Rule 12", value="[promo, selfpromo, invites]", inline=False)
        embed.add_field(name="Rule 13", value="[13, cheats, begging, buying, selling]", inline=False)
        embed.add_field(name="Rule 14", value="[14, guidelines, tos]", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(mod(bot))
    print('funlul')
