from discord.ext import commands
import discord


class Solois(commands.Cog):
    """Gods"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Solois")
    async def embed_god(self, ctx):
        url_image = "https://i.pinimg.com/564x/50/a0/18/50a018ed3c0826b61911cb415f8cb7fa.jpg"
        embed = discord.Embed(title="Solois ", description="Deus do conhecimento,sacreficios,e magia ", color=0x800000)

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="Feito por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(name="Hp", value="Imortal ")
        embed.add_field(name="Efeito", value="Dor Sangramento e incuravel", inline=False)
        embed.add_field(name="Aura", value="vermelho", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Solois(bot))
