from discord.ext import commands
import discord

class Kienzan(commands.Cog):
    """Kienzan"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Kienzan")
    async def Deckofmany(self, ctx):
        url_image = "https://pa1.narvii.com/6245/aa76a2b33696145865e0228ab7f4fcaf5f1ed306_hq.gif"
        embed = discord.Embed(title="Kienzan", description="2 discos cortantes que sao teleguiados", color=0xffff00)

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="Ki do Uzun", icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(name="2 Discos de energia são Teleguiados podem arcertar alvos diferentes", value="1d6 para cada disco", inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Kienzan(bot))