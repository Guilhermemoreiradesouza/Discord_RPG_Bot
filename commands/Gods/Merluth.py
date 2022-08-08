from discord.ext import commands
import discord


class Merluth(commands.Cog):
    """Gods"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Merluth")
    async def embed_god(self, ctx):
        url_image = "https://i.pinimg.com/564x/d4/cb/66/d4cb66a762dbe176f4d3146f89991820.jpg"
        embed = discord.Embed(title="Merluth ", description="Deusa da Luz, Fé , Merito", color=0xffffff)

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="Feito por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(name="Hp", value="Imortal ")
        embed.add_field(name="Efeito", value="Cura, Sanidade , cegueira", inline=False)
        embed.add_field(name="Aura", value="Branca", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Merluth(bot))
