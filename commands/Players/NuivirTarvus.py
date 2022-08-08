from discord.ext import commands
import discord


class NuivirTarvus(commands.Cog):
    """LOJAS"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="NuivirTarvus")
    async def ficha_player(self, ctx):
        url_image = "https://i.pinimg.com/564x/09/c2/52/09c25259be773c1cd19ff2335f40d6ea.jpg"
        embed = discord.Embed(
            title="Nuivir Tarvus ",
            description="Olday com flauta",
            color=0x808080)

        embed.set_author(
            name=self.bot.user.name,
            icon_url="http://pa1.narvii.com/6989/d37da4782fe2ad2c3fcf11f4036239b6a874ddber1-1077-1087_00.gif")

        embed.set_footer(
            text="Personagem do matt",
            icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(
            name="Idade",
            value="17",
            inline=True)

        embed.add_field(
            name="Força ",
            value="11",
            inline=True)

        embed.add_field(
            name="Velocidade ",
            value="26",
            inline=True)

        embed.add_field(
            name="Luta",
            value="74",
            inline=True)

        embed.add_field(
            name="Inteligência",
            value="28",
            inline=True)

        embed.add_field(
            name="Mirar",
            value="88",
            inline=True)

        embed.add_field(
            name="Percepção",
            value="59",
            inline=True)

        embed.add_field(
            name="Magia",
            value="Musica",
            inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(NuivirTarvus(bot))
