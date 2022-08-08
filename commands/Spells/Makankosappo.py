from discord.ext import commands
import discord

class Makankosappo(commands.Cog):
    """Makankosappo"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Makankosappo")
    async def Deckofmany(self, ctx):
        url_image = "https://i.pinimg.com/originals/03/19/d1/0319d101e81305f3bfd987397d5c1500.gif"
        embed = discord.Embed(title="Makankosappo", description="Um Golpe mortal capaz de perfurar tudo", color=0xff00ff)

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="Ki do Uzun", icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(name="Uma energia concentrada na ponta dos dedos ", value="Capaz de perfurar qualquer coisa", inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Makankosappo(bot))