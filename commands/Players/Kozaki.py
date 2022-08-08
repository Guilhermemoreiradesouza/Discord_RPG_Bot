from discord.ext import commands
import discord


class Kozaki(commands.Cog):
    """LOJAS"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Kozaki")
    async def ficha_player(self, ctx):
        url_image = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/786ed859-5b0d-47f0-bd45-7c30b6d1ba92/d9kzcay-01db9a3c-0b47-4279-a89b-6f18f14b8589.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzc4NmVkODU5LTViMGQtNDdmMC1iZDQ1LTdjMzBiNmQxYmE5MlwvZDlremNheS0wMWRiOWEzYy0wYjQ3LTQyNzktYTg5Yi02ZjE4ZjE0Yjg1ODkucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.0WqTEQU3BQcD15Tjyu4ITUBQxBL1PqwM_Gu6JIJS2JU"
        embed = discord.Embed(
            title="Kozaki ",
            description="Um Mink Habil com a espada",
            color=0x808080)

        embed.set_author(
            name=self.bot.user.name,
            icon_url="http://pa1.narvii.com/6989/d37da4782fe2ad2c3fcf11f4036239b6a874ddber1-1077-1087_00.gif")

        embed.set_footer(
            text="Personagem do nikko",
            icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(
            name="Idade",
            value="12",
            inline=True)

        embed.add_field(
            name="Força ",
            value="64",
            inline=True)

        embed.add_field(
            name="Velocidade ",
            value="98",
            inline=True)

        embed.add_field(
            name="Luta",
            value="41",
            inline=True)

        embed.add_field(
            name="Inteligência",
            value="18",
            inline=True)

        embed.add_field(
            name="Mirar",
            value="5",
            inline=True)

        embed.add_field(
            name="Percepção",
            value="45",
            inline=True)

        embed.add_field(
            name="Magia",
            value="Cãos",
            inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Kozaki(bot))
