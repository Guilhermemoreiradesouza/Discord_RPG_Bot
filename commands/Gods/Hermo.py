from discord.ext import commands
import discord


class Hermo(commands.Cog):
    """Gods"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Hermo")
    async def embed_god(self, ctx):
        url_image = "https://i.pinimg.com/564x/7d/d2/a1/7dd2a1b1047f2ef16e8f2e7fc32e436c.jpg"
        embed = discord.Embed(title="Hermo", description="Deus do Tempo e Destino ", color=0x808000)

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="Feito por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(name="Hp", value="Imortal ")
        embed.add_field(name="Efeito", value="Dejavu ou Dejavi", inline=False)
        embed.add_field(name="Aura", value="laranja", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Hermo(bot))
