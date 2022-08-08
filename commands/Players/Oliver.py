from discord.ext import commands
import discord


class Oliver(commands.Cog):
    """LOJAS"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Oliver")
    async def fichaplayer(self, ctx):
        url_image = "https://i.pinimg.com/564x/a0/d1/9b/a0d19bf21b123db0ed0337d8e82fe2a8.jpg"
        embed = discord.Embed(
            title="Oliver ",
            description="Oliver a Chuva",
            color=0xffff00)

        embed.set_author(
            name=self.bot.user.name,
            icon_url="https://i.pinimg.com/564x/50/b7/f4/50b7f4157454c112eb08a9d39b1be6ab.jpg")
        embed.set_footer(
            text="Personagem do Samuel",
            icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(
            name="Idade",
            value="15",
            inline=True)

        embed.add_field(
            name="Força ",
            value="50",
            inline=True)

        embed.add_field(
            name="Velocidade ",
            value="63", inline=True)

        embed.add_field(
            name="Luta",
            value="82",
            inline=True)

        embed.add_field(
            name="Inteligência",
            value="85",
            inline=True)

        embed.add_field(
            name="Mirar",
            value="77",
            inline=True)

        embed.add_field(
            name="Percepção",
            value="60",
            inline=True)

        embed.add_field(
            name="Magia",
            value="Eletricidade",
            inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Oliver(bot))
