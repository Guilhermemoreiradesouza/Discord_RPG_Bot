from discord.ext import commands
import discord


class Gabriza(commands.Cog):
    """LOJAS"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Gabriza")
    async def fichaplayer(self, ctx):
        url_image = "https://i.pinimg.com/564x/75/cf/c0/75cfc0af3f1a5a234b30309cb59437d7.jpg"
        embed = discord.Embed(
            title="Gabriza ",
            description="Senhor Do Sol",
            color=0xffffff)

        embed.set_author(
            name=self.bot.user.name,
            icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEjTqe74s2AuIXezEgdSL10d_bSBvNmbYwng&usqp=CAU")
        embed.set_footer(
            text="Personagem do Gabriza",
            icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(
            name="Idade",
            value="23",
            inline=True)
        embed.add_field(
            name="Força ",
            value="29",
            inline=True)
        embed.add_field(
            name="Velocidade ",
            value="71",
            inline=True)
        embed.add_field(
            name="Luta",
            value="86",
            inline=True)
        embed.add_field(
            name="Inteligência",
            value="63",
            inline=True)
        embed.add_field(
            name="Mirar",
            value="44",
            inline=True)
        embed.add_field(
            name="Percepção",
            value="79",
            inline=True)
        embed.add_field(
            name="Magia",
            value="Quantos mais forte o sol se mostra mais forte ele se torna",
            inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Gabriza(bot))
