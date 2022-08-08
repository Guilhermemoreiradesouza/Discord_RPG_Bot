from discord.ext import commands
import discord


class Monog(commands.Cog):
    """Gods"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Monog")
    async def embed_god(self, ctx):
        url_image = "https://i.pinimg.com/564x/3a/28/4e/3a284e44d4a08eca2b7f773c40df7c16.jpg"
        embed = discord.Embed(title="Monog ", description="Deus do Caos e Equilibrio ", color=0x800080)

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="Feito por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(name="Hp", value="Imortal ")
        embed.add_field(name="Efeito", value="Troca de corpos", inline=False)
        embed.add_field(name="Aura", value="Roxo", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Monog(bot))
