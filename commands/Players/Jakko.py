from discord.ext import commands
import discord


class Jakko(commands.Cog):
    """LOJAS"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Jakko")
    async def fichaplayer(self, ctx):
        url_image = "https://i1.wp.com/streamie.com.br/wp-content/uploads/2018/02/img-reinhardt-cinematica.png"
        embed = discord.Embed(
            title="Jakko ",
            description="Jakko a Maquina de Combate",
            color=0xffff00)

        embed.set_author(
            name=self.bot.user.name,
            icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdCjVoGHAhuPbR1yX5SOn5C0L8GcXF3NUR6Q&usqp=CAU")

        embed.set_footer(
            text="Personagem do Marcus",
            icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(
            name="Idade",
            value="40",
            inline=True)

        embed.add_field(
            name="Força ",
            value="88",
            inline=True)

        embed.add_field(
            name="Velocidade ",
            value="75",
            inline=True)

        embed.add_field(
            name="Luta",
            value="89",
            inline=True)

        embed.add_field(
            name="Inteligência",
            value="61",
            inline=True)

        embed.add_field(
            name="Mirar", value="75",
            inline=True)

        embed.add_field(
            name="Percepção",
            value="29",
            inline=True)

        embed.add_field(
            name="Magia",
            value="Machado Foguete e Escuto Magico",
            inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Jakko(bot))
