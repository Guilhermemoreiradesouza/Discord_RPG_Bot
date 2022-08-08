from discord.ext import commands
import discord

class Son_Uzun(commands.Cog):
    """LOJAS"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Son_Uzun")
    async def ficha_player(self, ctx):

        url_image = "http://pm1.narvii.com/7045/c5f470189c3d44243a9db929b502075b87228270r1-1024-1024v2_00.jpg"

        embed = discord.Embed(
            title="Son Uzun ",
            description="O arcanista de outro planeta",
            color=0xffff00)

        embed.set_author(
            name=self.bot.user.name,
            icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdCjVoGHAhuPbR1yX5SOn5C0L8GcXF3NUR6Q&usqp=CAU")

        embed.set_footer(
            text="Personagem do Spaz",
            icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(
            name="Idade",
            value="20",
            inline=True)

        embed.add_field(
            name="Força ",
            value="99",
            inline=True)

        embed.add_field(
            name="Velocidade ",
            value="57",
            inline=True)

        embed.add_field(
            name="Luta",
            value="81",
            inline=True)

        embed.add_field(
            name="Inteligência",
            value="19",
            inline=True)

        embed.add_field(
            name="Mirar",
            value="39",
            inline=True)

        embed.add_field(
            name="Percepção",
            value="16",
            inline=True)

        embed.add_field(
            name="Magia",
            value="Energia",
            inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Son_Uzun(bot))
