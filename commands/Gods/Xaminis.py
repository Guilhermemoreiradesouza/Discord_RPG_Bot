from discord.ext import commands
import discord


class Xaminis(commands.Cog):
    """Gods"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Xaminis")
    async def embed_god(self, ctx):
        url_image = "https://soulsofhellscytherpg.weebly.com/uploads/1/2/7/9/127958332/1efce141dbac44ffa4f35dce4b72cd7b_orig.jpg"
        embed = discord.Embed(title="Xaminis ", description="Deus da Escuridão, Dor , Trapaça", color=0x000000)

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="Feito por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(name="Hp", value="Imortal ")
        embed.add_field(name="Efeito", value="Trapaça e tontura", inline=False)
        embed.add_field(name="Aura", value="Preta", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Xaminis(bot))
