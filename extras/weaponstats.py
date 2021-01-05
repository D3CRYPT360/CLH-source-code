import discord
from discord import colour
from discord.ext import commands
from utils.requesting import Weapon
import DiscordUtils



class weaponStats(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def weapon(self, ctx, weapon):
        json_data = Weapon()
        weapon = weapon.capitalize()
        if weapon == "Melee":
            return
        Str = ''
        for i in range(len(json_data['data'])):
            if json_data['data'][i]['displayName'] == weapon:
                for x in range(len(json_data['data'][i]['weaponStats']['damageRanges'])):
                    Range = json_data['data'][i]['weaponStats']['damageRanges']
                    Str += ("```py" +
                            f"\n Damage from range {Range[x]['rangeStartMeters']}M to {Range[x]['rangeEndMeters']}M is "+
                            "\n Head Damage: {}".format(Range[x]['headDamage']) +
                            "\n Body Damage: {}".format(Range[x]['bodyDamage']) +
                            "\n Leg Damage: {}```".format(Range[x]['bodyDamage'])
                        )
                embed1 = discord.Embed(
                    colour = discord.Color.dark_theme(),
                    title = "__{}__".format(json_data['data'][i]['displayName'])
                )
                embed1.add_field(name="__{} Stats__".format(json_data['data'][i]['displayName']),
                value=(
                    "```py"+
                    "\n Firerate: {}".format(json_data['data'][i]['weaponStats']['fireRate']) +
                    "\n Magazine size: {}".format(json_data['data'][i]['weaponStats']['magazineSize']) +
                    "\n First Bullet Inaccuracy: {}".format(json_data['data'][i]['weaponStats']['firstBulletAccuracy']) +
                    "\n Wall Penetration: {}```".format((json_data['data'][i]['weaponStats']['wallPenetration']).replace("EWallPenetrationDisplayType::", '')))
                )
                embed1.set_image(url="{}".format(json_data['data'][i]['displayIcon']))

                embed2 = discord.Embed(
                    colour = discord.Color.dark_theme(),
                    title = "__{}__".format(json_data['data'][i]['displayName'])
                )
                embed2.add_field(name="__{} Damage from range chart__".format(json_data['data'][i]['displayName']),value= Str)
                embed2.set_image(url="{}".format(json_data['data'][i]['displayIcon']))
                
                embed3 = discord.Embed(
                    colour = discord.Color.dark_theme(),
                    title = "__{}__".format(json_data['data'][i]['displayName'])
                )
                embed3.add_field(name="__{} ADS stats__".format(json_data['data'][i]['displayName']),
                value=(
                    "```py" +
                    "\n Zoom Multiplier: {}".format(json_data['data'][x]['weaponStats']['adsStats']['zoomMultiplier']) +
                    "\n Fire Rate: {}".format(json_data['data'][x]['weaponStats']['adsStats']['fireRate']) +
                    "\n Run Speed Multiplier: {}".format(json_data['data'][x]['weaponStats']['adsStats']['runSpeedMultiplier']) +
                    "\n Burst Count: {}".format(json_data['data'][x]['weaponStats']['adsStats']['burstCount']) +
                    "\n First Bullet Inaccuracy: {}```".format(json_data['data'][x]['weaponStats']['adsStats']['firstBulletAccuracy'])) 
                )
                embed3.set_image(url="{}".format(json_data['data'][i]['displayIcon']))

                paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, auto_footer = True)
                paginator.add_reaction('⬅️', "back")
                paginator.add_reaction('➡️', "next")
                embeds = [embed1, embed2, embed3]
                await paginator.run(embeds)

"""
            "rangeStartMeters": 30,
            "rangeEndMeters": 50,damageRanges
            "headDamage": 77.5,
            "bodyDamage": 31,
            "legDamage": 26.35
          }
        ]
      },
"""
"""

"""
def setup(bot):
    bot.add_cog(weaponStats(bot))
    print("weaponstats.py loaded")