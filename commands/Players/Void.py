from discord.ext import commands
import discord


class Void(commands.Cog):
    """LOJAS"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Void")
    async def ficha_player(self, ctx):

        url_image = "https://i.pinimg.com/564x/38/c0/da/38c0dae2750b397164a3ab586f602233.jpg"

        embed = discord.Embed(
            title="Void ",
            description="Senhor Do Vazio",
            color=0x808080)

        embed.set_author(
            name=self.bot.user.name,
            icon_url="https://i.pinimg.com/564x/6a/7f/44/6a7f445d17da5674f089a2d4219e7071.jpg")

        embed.set_footer(
            text="Personagem do Bio",
            icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(
            name="Idade",
            value="9",
            inline=True)

        embed.add_field(
            name="Força ",
            value="64",
            inline=True)

        embed.add_field(
            name="Velocidade ",
            value="95",
            inline=True)

        embed.add_field(
            name="Luta",
            value="100",
            inline=True)

        embed.add_field(
            name="Inteligência",
            value="99",
            inline=True)

        embed.add_field(
            name="Mirar",
            value="69",
            inline=True)

        embed.add_field(
            name="Percepção",
            value="64",
            inline=True)

        embed.add_field(
            name="Magia",
            value="Modifica a Mente e a Realidade",
            inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Void(bot))
