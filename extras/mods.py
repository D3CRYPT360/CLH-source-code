import discord
from discord.ext import commands


class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=["r"], hidden=True)
    @commands.has_guild_permissions(ban_members=True)
    async def rule(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("/r [rule number or keyword in rule]\n/r tags <- [to see all the tags]")


    @rule.command(aliases=["1", "harrasment", "discrimination", "race"])
    @commands.has_guild_permissions(ban_members=True)
    async def _1(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/748075193154404436/768451050955997196/unknown.png")

    @rule.command(aliases=["2", "english", "nonenglish"])
    @commands.has_guild_permissions(ban_members=True)
    async def _2(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/748075193154404436/768451194707640340/unknown.png")

    @rule.command(aliases=["3", "nsfw"])
    @commands.has_guild_permissions(ban_members=True)
    async def _3(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/748075193154404436/768451506403278861/unknown.png")

    @rule.command(aliases=["4", "pfp", "profile", "username", "nickname", "status"])
    @commands.has_guild_permissions(ban_members=True)
    async def _4(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/748075193154404436/768451788855967764/unknown.png")

    @rule.command(aliases=["5", "impersonation", "imp"])
    @commands.has_guild_permissions(ban_members=True)
    async def _5(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/748075193154404436/768452225173291038/unknown.png")

    @rule.command(aliases=["6", "religion", "politics", "controversial"])
    @commands.has_guild_permissions(ban_members=True)
    async def _6(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/748075193154404436/768452607970115604/unknown.png")

    @rule.command(aliases=["7", "spam", "emojispam", "links", "mention"])
    @commands.has_guild_permissions(ban_members=True)
    async def _7(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/748075193154404436/768452945498734642/unknown.png")

    @rule.command(aliases=["8", "topic"])
    @commands.has_guild_permissions(ban_members=True)
    async def _8(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/748075193154404436/768453342111465502/unknown.png")

    @rule.command(aliases=["9", "dox", "doxxing", "doxx", "personal"])
    @commands.has_guild_permissions(ban_members=True)
    async def _9(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/748075193154404436/768453722539032607/unknown.png")

    @rule.command(aliases=["10", "bug", "bugs", "exploit", "exploitation"])
    @commands.has_guild_permissions(ban_members=True)
    async def _10(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/748075193154404436/768454035354943499/unknown.png")

    @rule.command(aliases=["11", "riot", "dev", "devs", "riotping", "devping"])
    @commands.has_guild_permissions(ban_members=True)
    async def _11(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/748075193154404436/768454319078506566/unknown.png")

    @rule.command(aliases=["12", "promo", "selfpromo", "invites"])
    @commands.has_guild_permissions(ban_members=True)
    async def _12(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/748075193154404436/768454375446151188/unknown.png")

    @rule.command(aliases=["tag"])
    @commands.has_guild_permissions(ban_members=True)
    async def tags(self, ctx):
        await ctx.send("```\nTags for the rules\n1=[harrasment, discrimination, race]\n2=[english, nonenglish]\n3=[nsfw]\n4=[pfp, profile, username, nickname, status]\n5=[impersonation, imp]\n6=[religion, politics, controversial]\n7=[spam, emojispam, links, mention]\n8=[topic]\n9=[dox, doxxing, doxx, personal]\n10=[bug, bugs, exploit, exploitation]\n11=[riot, dev, devs, riotping, devping]\n12=[promo, selfpromo, invites]\n```")

def setup(bot):
    bot.add_cog(mod(bot))
    print('funlul')
