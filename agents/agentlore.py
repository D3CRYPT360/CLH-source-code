import discord
from discord.ext import commands

class __Agent_lore__(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #BRIMBUDDY#
    #brimstone off#
    @commands.command(aliases = ['brim' , 'sarge'], description='Shows the Official & Unofficial Brimstone lore')
    async def brimstone(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_gold(),
            title=("**Official Brimstone Lore** : https://discordapp.com/channels/708983243847761931/727953100110823446/742455802035437568\n**Unofficial Brimstone Lore** : https://discordapp.com/channels/708983243847761931/747484591836758127/748649585211211878")
        )
        embed.add_field(name = "__Agent Info__", value="```Name: Brimstone\nCodename: Sarge\nAgent ID: 1\nCountry: USA\nType: Controller```", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/746327425759182908/765111848823029760/TX_Character_Thumb_Sarge.png")
        await ctx.send(embed=embed)

    #VIPER
    #viper off#
    @commands.command(aliases = ['sabine' , 'pandemic'], description="Shows the Official & Unofficial Viper lore")
    async def viper(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_gold(),
            title=("**Official Viper Lore** : https://discordapp.com/channels/708983243847761931/727953100110823446/742456639277236294\n**Unoficial Viper Lore** : https://discordapp.com/channels/708983243847761931/747484591836758127/748654881392296067")
        )
        embed.add_field(name="__Agent Info__", value="```Name: Viper\nCodename: Pandemic (scrapped)\nReal Name: Sabine\nAgent ID: 02\nCountry: USA\nType: Controller```", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/746327425759182908/765111844041523210/TX_Character_Thumb_Pandemic.png")
        await ctx.send(embed=embed)

    #OMEN
    #omen off#
    @commands.command(aliases = ['wraith'], description="Shows the Official & Unofficial Omen lore")
    async def omen(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_gold(),
            title=("**Official Omen Lore** : https://discordapp.com/channels/708983243847761931/727953100110823446/742457266254381186\n**Unofficial Omen Lore** : https://discordapp.com/channels/708983243847761931/747484591836758127/748667838100668549")
        )
        embed.add_field(name="__Agent Info__", value="```Name: Omen\nCodename: Wraith (scrapped)\nReal Name: ???\nAgent ID: 03\nCountry: ???\nType: Controller```", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/746327425759182908/765111852866207744/TX_Character_Thumb_Wraith.png")
        await ctx.send(embed=embed)

    #KILLJOY#
    #killjoy off#
    @commands.command(aliases = ['kj'], description="Shows the Official & Unofficial Killjoy lore")
    async def killjoy(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_gold(),
            title=("**Official Killjoy Lore** : https://discordapp.com/channels/708983243847761931/727953100110823446/742457949313695774\n**Unofficial Killjoy Lore** : https://discordapp.com/channels/708983243847761931/747484591836758127/748695653500059748")
        )
        embed.add_field(name="__Agent Info__", value="```Name: Killjoy\nCodename: Killjoy\nRealname: ???\nAgent ID: 04\nCountry: Germany\nType: Sentinel```", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/746327425759182908/765111844637114418/TX_Character_Thumb_Killjoy.png")
        await ctx.send(embed=embed)

    #CYPHER
    #Cypher off#
    @commands.command(aliases = ['aamir' ,'gumshoe'], description="Shows the Official & Unofficial Cypher lore")
    async def cypher(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_gold(),
            title=("**Official Cypher Lore** : https://discordapp.com/channels/708983243847761931/727953100110823446/742696637708763138\n**Unofficial Cypher Lore** : https://discordapp.com/channels/708983243847761931/747484591836758127/748711251928154232")
        )
        embed.add_field(name="__Agent Info__", value="```Name: CYPHER\nCodename: Gumshoe (scrapped)\nReal Name: Aamir\nAgent ID: 05\nCountry: Morocco\nType: Sentinel```", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/746327425759182908/765111840057327636/TX_Character_Thumb_Gumshoe.png")
        await ctx.send(embed=embed)

    #SOVA
    #Sova off#
    @commands.command(aliases = ['hunter', 'constant', 'constantvalorant'], description="Shows the Official & Unofficial Sova lore")
    async def sova(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_gold(),
            title=("**Official Sova Lore** : https://discordapp.com/channels/708983243847761931/727953100110823446/742696788128956466\n**Unofficial Sova Lore** : https://discordapp.com/channels/708983243847761931/747484591836758127/748860067549413427")
        )
        embed.add_field(name="__Agent Info__", value="```Name: Sova\nCodename: Hunter\nReal Name: ???\nAgent ID: 06\nCountry: Russia\nType: Initiator```", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/746327425759182908/765111841344454687/TX_Character_Thumb_Hunter.png")
        await ctx.send(embed=embed)

    #SAGE
    #Sage off#
    @commands.command(aliases = ['thorne'], description="Shows the Official & Unofficial sage lore")
    async def sage(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_gold(),
            title=("**Official Sage Lore** : https://discordapp.com/channels/708983243847761931/727953100110823446/742697064365949030\n**Unofficial Sage Lore** : https://discordapp.com/channels/708983243847761931/747484591836758127/748906193757405216")
        )
        embed.add_field(name="__Agent Info__", value="```Name: Sage\nCodename: Thorne (scrapped)\nReal Name: ???\nAgent ID: 07\nCountry: China\nType: Sentinel```", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/746327425759182908/765111850316333076/TX_Character_Thumb_Thorne.png")
        await ctx.send(embed=embed)

    #PHX
    #Phoenix off#
    @commands.command(aliases = ['grant' , 'phx'], description="Shows the Official & Unoffical Phoenix lore")
    async def phoenix(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_gold(),
            title=("**Official Phoenix Lore** : https://discordapp.com/channels/708983243847761931/727953100110823446/742698018012266547\n**Unofficial Phoenix Lore** : https://discordapp.com/channels/708983243847761931/747484591836758127/748979255374774494")
        )
        embed.add_field(name="__Agent Info__", value="```Name: Phoenix\nCodename: Phoenix\nReal Name: Grant Galloway\nAgent ID: 09\nCountry: United Kingdom\nType: Duelist```", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/746327425759182908/765111844817600512/TX_Character_Thumb_Phoenix.png")
        await ctx.send(embed=embed)

    #JETT
    #jett official#
    @commands.command(aliases = ['wushu', 'hawks', 'junhee'], description="Shows the Official & Unofficial Jett lore")
    async def jett(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_gold(),
            title=("**Official Jett Lore** : https://discordapp.com/channels/708983243847761931/727953100110823446/742698186686332929\n**Unofficial Jett Lore** : https://discordapp.com/channels/708983243847761931/747484591836758127/748990254010204311")
        )
        embed.add_field(name="__Agent Info__", value="```Name: Jett\nCodename: Hawks\nScrapped Codename: Wushu\nAgent ID: 10\nReal Name: Joon Hee\nCountry: South Korea\nType: Duelist```", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/759101153073692722/765112123856257064/TX_Character_Thumb_Wushu.png")
        await ctx.send(embed=embed)

    #REYNA
    #Reyna off#
    @commands.command(aliases = ['vampire'], description="Shows the Official & Unofficial Reyna lore")
    async def reyna(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_gold(),
            title=("**Official Reyna Lore** : https://discordapp.com/channels/708983243847761931/727953100110823446/742698335168888874\n**Unofficial Reyna Lore** : https://discordapp.com/channels/708983243847761931/747484591836758127/749018798543339572")
        )
        embed.add_field(name="__Agent Info__", value="```Name: Reyna\nCodename: Vampire (scrapped)\nReal Name: ???\nAgent ID: 11\nCountry: Mexico\nType: Duelist```", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/759101153073692722/765112192097189908/TX_Character_Thumb_Vampire.png")
        await ctx.send(embed=embed)

     #RAZE
    #Raze off#
    @commands.command(aliases = ['clay', 'trash'], description="Shows the Official & Unofficial Raze lore")
    async def raze(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_gold(),
            title=("**Official Raze Lore** : https://discordapp.com/channels/708983243847761931/727953100110823446/742698493680025611\n**Unofficial Raze Lore** : https://discordapp.com/channels/708983243847761931/747484591836758127/749202008090869850")
        )
        embed.add_field(name="__Agent Info__", value="```Name: Raze\nCodename: Clay (scrapped)\nReal Name: ???\nAgent ID: 12\nCountry: Brazil\nType: Duelist```", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/759101153073692722/765112104155086858/TX_Character_Thumb_Raze.png")
        await ctx.send(embed=embed)



    #Breach#
    @commands.command(aliases = ['cabbage' , 'lettuce'], description='Shows the Official & Unofficial Breach lore')
    async def breach(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_gold(),
            title=("**Official Breach Lore** : https://discordapp.com/channels/708983243847761931/727953100110823446/742698622101225644\n**Unofficial Breach Lore** : https://discordapp.com/channels/708983243847761931/747484591836758127/749222091219402842")
        )
        embed.add_field(name="__Agent Info__", value="```Name: Breach\nCodename: Breach\nReal Name: ???\nAgent ID: 13\nCountry: Sweden\nType: Initiator```", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/759101153073692722/765112128301432832/TX_Character_Thumb_Breach.png")
        await ctx.send(embed=embed)


    #SKYE#
    @commands.command(aliases = ['sky' , 'upsidedown', "mate", 'guide'])
    async def skye(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_gold(),
            title=("**Official Skye Lore** : https://discordapp.com/channels/708983243847761931/727953100110823446/770698138972454932\n**Unofficial Skye Lore** : https://discordapp.com/channels/708983243847761931/747484591836758127/763465241966542908")
        )
        embed.add_field(name="__Agent Info__", value="```Name: Skye\nCodename: Guide (scrapped)\nReal Name: ???\nAgent ID: 14\nCountry: Australia\nType: Initiator```", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745696342260711516/770696329462415360/TX_Character_Thumb_Guide_256.png")
        await ctx.send(embed=embed)

     #rift lore
    @commands.command(description="Shows the lore about rifts")
    async def rift(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_gold(),
            title=("**Rift Lore** : https://discord.com/channels/708983243847761931/727811131254505523/748854274343043152")
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745696342260711516/767025310285430824/Spray_Dark_Side_Beyond.gif")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(__Agent_lore__(bot))
    print('Agent lore is loaded')
