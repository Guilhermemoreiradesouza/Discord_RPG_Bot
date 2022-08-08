from discord.ext import commands
import discord


class Samuel(commands.Cog):
    """LOJAS"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Samuel")
    async def ficha_player(self, ctx):
        url_image = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/a7564bda-842b-4b8e-a21b-27dab68a6ac6/dc12d5f-1b1f4c08-e847-4ed3-b61b-0a19bdc69388.png/v1/fill/w_234,h_350,strp/fiery_sauron_by_kaprriss_dc12d5f-350t.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTUwMCIsInBhdGgiOiJcL2ZcL2E3NTY0YmRhLTg0MmItNGI4ZS1hMjFiLTI3ZGFiNjhhNmFjNlwvZGMxMmQ1Zi0xYjFmNGMwOC1lODQ3LTRlZDMtYjYxYi0wYTE5YmRjNjkzODgucG5nIiwid2lkdGgiOiI8PTEwMDMifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.u5igQmA_NsyjQthWn6PIuzjNgBQIJQckdpdvjUumqf0"

        embed = discord.Embed(
            title="Samuel ",
            description="Emperador das Chamas",
            color=0xf08000)

        embed.set_author(
            name=self.bot.user.name,
            icon_url="https://i.pinimg.com/564x/6a/7f/44/6a7f445d17da5674f089a2d4219e7071.jpg")

        embed.set_footer(
            text="Personagem do Samuel",
            icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(
            name="Idade",
            value="18",
            inline=True)

        embed.add_field(
            name="Força ",
            value="51",
            inline=True)

        embed.add_field(
            name="Velocidade ",
            value="44",
            inline=True)

        embed.add_field(
            name="Luta",
            value="60",
            inline=True)

        embed.add_field(
            name="Inteligência",
            value="47",
            inline=True)

        embed.add_field(
            name="Mirar",
            value="57",
            inline=True)

        embed.add_field(
            name="Percepção",
            value="2",
            inline=True)

        embed.add_field(
            name="Magia",
            value="Manipular Fogo",
            inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Samuel(bot))
