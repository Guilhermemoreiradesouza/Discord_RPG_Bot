from discord.ext import commands
import discord


class SenhorAtral(commands.Cog):
    """LOJAS"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Senhor-Astral")
    async def ficha_player(self, ctx):

        url_image = "https://c4.wallpaperflare.com/wallpaper/798/305/101/fate-series-fate-grand-order-goetia-fate-grand-order-hd-wallpaper-preview.jpg"

        embed = discord.Embed(
            title="Senhor-Astral ",
            description="Senhor Da materia",
            color=0x808080)

        embed.set_author(
            name=self.bot.user.name,
            icon_url="https://i.pinimg.com/564x/6a/7f/44/6a7f445d17da5674f089a2d4219e7071.jpg")

        embed.set_footer(
            text="Personagem do Breno",
            icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(
            name="Idade",
            value="???",
            inline=True)

        embed.add_field(
            name="Força ",
            value="56",
            inline=True)

        embed.add_field(
            name="Velocidade ",
            value="75",
            inline=True)

        embed.add_field(
            name="Luta",
            value="55",
            inline=True)

        embed.add_field(
            name="Inteligência",
            value="7",
            inline=True)

        embed.add_field(
            name="Mirar",
            value="16",
            inline=True)

        embed.add_field(
            name="Percepção",
            value="3",
            inline=True)

        embed.add_field(
            name="Magia",
            value="Cria coisas no plano astral",
            inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(SenhorAtral(bot))
