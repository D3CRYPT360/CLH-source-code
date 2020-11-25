import discord
from discord.ext import commands
import DiscordUtils



class beta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(hidden=True)
    async def beta(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("/beta (agent name) *works only one agents that has been in the game since beta*")
            
    @beta.command(aliases=["brim"])
    async def brimstone(self, ctx):
        
        embed1 = discord.Embed(colour=discord.Colour.orange())
        embed1.set_image(url= "https://cdn.discordapp.com/attachments/747483388415311883/750327062505717791/Coffee.png")
        
        embed2 = discord.Embed(colour=discord.Colour.orange())
        embed2.set_image(url = "https://cdn.discordapp.com/attachments/747483388415311883/750327090166890526/Open_Up_The_Sky.png")
        
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, auto_footer = True)
        paginator.add_reaction('⬅️', "back")
        paginator.add_reaction('➡️', "next")
        embeds = [embed1, embed2,]
        await paginator.run(embeds)
        
    @beta.command(aliases = ['thorne'])
    async def sage(self, ctx):
        
        embed1 = discord.Embed(colour=discord.Colour.teal())
        embed1.set_image(url= "https://cdn.discordapp.com/attachments/747483388415311883/750326961708204092/Balanced.png")
        
        embed2 = discord.Embed(colour=discord.Colour.teal())
        embed2.set_image(url = "https://cdn.discordapp.com/attachments/747483388415311883/750326973586472970/Harmony.png")
        
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, auto_footer = True)
        paginator.add_reaction('⬅️', "back")
        paginator.add_reaction('➡️', "next")
        embeds = [embed1, embed2,]
        await paginator.run(embeds)
        
    @beta.command(aliases=["lettuce","cabbage"])
    async def breach(self, ctx):
        
        embed1 = discord.Embed(colour=discord.Colour.dark_orange())
        embed1.set_image(url= "https://cdn.discordapp.com/attachments/747483388415311883/750327494321766411/Off_Your_Feet.png")
        
        embed2 = discord.Embed(colour=discord.Colour.dark_orange())
        embed2.set_image(url = "https://cdn.discordapp.com/attachments/747483388415311883/750327511837311076/Breach_2_dog.png")
        
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, auto_footer = True)
        paginator.add_reaction('⬅️', "back")
        paginator.add_reaction('➡️', "next")
        embeds = [embed1, embed2,]
        await paginator.run(embeds)
        
    @beta.command(aliases = ['aamir' ,'gumshoe'])
    async def cypher(self, ctx):
        
        embed1 = discord.Embed(colour=discord.Colour.dark_theme())
        embed1.set_image(url= "https://cdn.discordapp.com/attachments/747483388415311883/750327597644382298/cypher_1_m1.png")
        
        embed2 = discord.Embed(colour=discord.Colour.dark_theme())
        embed2.set_image(url = "https://cdn.discordapp.com/attachments/747483388415311883/750327609199689808/Cypher_card.png")
        
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, auto_footer = True)
        paginator.add_reaction('⬅️', "back")
        paginator.add_reaction('➡️', "next")
        embeds = [embed1, embed2,]
        await paginator.run(embeds)
    
    @beta.command(aliases = ['grant' , 'phx'])
    async def phoenix(self, ctx):
        
        embed1 = discord.Embed(colour=discord.Colour.orange())
        embed1.set_image(url= "https://cdn.discordapp.com/attachments/747483388415311883/750327686831800430/Phoenixs_Sun.png")
        
        embed2 = discord.Embed(colour=discord.Colour.orange())
        embed2.set_image(url = "https://cdn.discordapp.com/attachments/747483388415311883/750327701642018887/Phoenix_Down.png")
        
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, auto_footer = True)
        paginator.add_reaction('⬅️', "back")
        paginator.add_reaction('➡️', "next")
        embeds = [embed1, embed2,]
        await paginator.run(embeds)
        
    @beta.command(aliases = ['wushu'])
    async def jett(self, ctx):
        
        embed1 = discord.Embed(colour=discord.Colour.orange())
        embed1.set_image(url= "https://cdn.discordapp.com/attachments/747483388415311883/750327767425351721/Jett_Card.webp")
        
        embed2 = discord.Embed(colour=discord.Colour.orange())
        embed2.set_image(url = "https://cdn.discordapp.com/attachments/747483388415311883/750327779127459840/Jett_knife.jpg")
        
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, auto_footer = True)
        paginator.add_reaction('⬅️', "back")
        paginator.add_reaction('➡️', "next")
        embeds = [embed1, embed2,]
        await paginator.run(embeds)
        
    @beta.command(aliases = ['hunter', 'constant', 'constantvalorant'])
    async def sova(self, ctx):
        
        embed1 = discord.Embed(colour=discord.Colour.blue())
        embed1.set_image(url= "https://cdn.discordapp.com/attachments/747483388415311883/750327862162227210/Sova_Pose.png")
        
        embed2 = discord.Embed(colour=discord.Colour.blue())
        embed2.set_image(url = "https://cdn.discordapp.com/attachments/747483388415311883/750327874069725244/Sova_Ult.png")
        
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, auto_footer = True)
        paginator.add_reaction('⬅️', "back")
        paginator.add_reaction('➡️', "next")
        embeds = [embed1, embed2,]
        await paginator.run(embeds)
        
    @beta.command(aliases = ['wraith'])
    async def omen(self, ctx):
        
        embed1 = discord.Embed(colour=discord.Colour.purple())
        embed1.set_image(url= "https://cdn.discordapp.com/attachments/747483388415311883/750327950020313088/Omen_Teleport.png")
        
        embed2 = discord.Embed(colour=discord.Colour.purple())
        embed2.set_image(url = "https://cdn.discordapp.com/attachments/747483388415311883/750328152936677376/Omen_Ult.webp")
        
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, auto_footer = True)
        paginator.add_reaction('⬅️', "back")
        paginator.add_reaction('➡️', "next")
        embeds = [embed1, embed2,]
        await paginator.run(embeds)
        
    @beta.command(aliases = ['sabine' , 'pandemic'])
    async def viper(self, ctx):
        
        embed1 = discord.Embed(colour=discord.Colour.green())
        embed1.set_image(url= "https://cdn.discordapp.com/attachments/747483388415311883/750328266208051260/Viper_Lab_Coat.png")
        
        embed2 = discord.Embed(colour=discord.Colour.green())
        embed2.set_image(url = "https://cdn.discordapp.com/attachments/747483388415311883/750328404380876901/Viper_Ult.webp")
        
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, auto_footer = True)
        paginator.add_reaction('⬅️', "back")
        paginator.add_reaction('➡️', "next")
        embeds = [embed1, embed2,]
        await paginator.run(embeds)
    
    
    @beta.command(aliases=['kj'])
    async def killjoy(self, ctx):
        embed1 = discord.Embed(colour=discord.Colour.gold())
        embed1.set_image(url= "https://cdn.discordapp.com/attachments/746327425759182908/765113285460099092/TX_PlayerCard_Default_Wasd01_large.png")
        await ctx.send(embed=embed1)
        
    @beta.command(aliases=['clay'])
    async def raze(self, ctx):
        embed1 = discord.Embed(colour=discord.Colour.dark_magenta())
        embed1.set_image(url= "https://cdn.discordapp.com/attachments/747483388415311883/750328574078091395/Raze_Up.png")
        await ctx.send(embed=embed1)
        
        
def setup(bot):
    bot.add_cog(beta(bot))
    print('Help is Ready')

