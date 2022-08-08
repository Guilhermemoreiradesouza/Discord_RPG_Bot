from discord.ext import commands
import discord


class ConsumirMagia(commands.Cog):
    """Consumir_Magia"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Consumir_Magia")
    async def deckofmany(self, ctx):
        url_image = "https://64.media.tumblr.com/6a8383323ec8fb4270694d990c2c6b29/tumblr_oyvfo4xbaD1ti1x5no1_540.gifv"

        embed = discord.Embed(
            title="Consumir Magia",
            description="Absorve magia de coisas e adciona ao seu corpo",
            color=0xf0ff00)

        embed.set_author(
            name=self.bot.user.name,
            icon_url=self.bot.user.avatar_url)

        embed.set_footer(
            text="Tecnologia do Jakko",
            icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(
            name="adapta magia ao seu corpo ",
            value="o efeito se torna permanente, uma magia por parte do corpo",
            inline=True)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ConsumirMagia(bot))
