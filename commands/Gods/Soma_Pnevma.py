from discord.ext import commands
import discord


class SomaePnevma(commands.Cog):
    """Gods"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sóma|pnévma")
    async def embed_god(self, ctx):
        url_image = "https://i.pinimg.com/564x/d9/db/12/d9db1240875988810753a76cbe9e1bc3.jpg"
        embed = discord.Embed(title="Sóma e Pnévma ", description="Sóma deus do corpo , Pnévma Deus do espirito",
                              color=0x808080)

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="Feito por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(name="Hp", value="Imortal ")
        embed.add_field(name="Efeito", value="Polymorfia fisica, Polymorfia Magica", inline=False)
        embed.add_field(name="Aura", value="Cinza", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(SomaePnevma(bot))
