from discord.ext import commands
import discord


class Silf(commands.Cog):
    """LOJAS"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Silf")
    async def embed_loja(self, ctx):
        url_image = "https://i.pinimg.com/564x/bf/19/da/bf19dafee4b4322496b065bf88b411ee.jpg"
        embed = discord.Embed(
            title="Vendedor ambulante de poçoes ",
            description="Uma poção não deixa na mão",
            color=0x808080)

        embed.set_author(
            name=self.bot.user.name,
            icon_url="https://i.pinimg.com/564x/ff/52/82/ff52826611e86baba8ead4f4fea5728d.jpg")
        embed.set_footer(
            text="Loja De Poçoes",
            icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(
            name="Inventario",
            value="Poçoes")
        embed.add_field(
            name="Poçoes",
            value="poçoes de utilidade",
            inline=False)
        embed.add_field(
            name="Venenos",
            value="Poçoes de debuff",
            inline=False)
        embed.add_field(
            name="Remedios",
            value="Em caso de feridas ou Doenças",
            inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Silf(bot))
