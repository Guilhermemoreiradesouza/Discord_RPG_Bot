from discord.ext import commands
import discord

class kamehameha(commands.Cog):
    """kamehameha"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kamehameha")
    async def Deckofmany(self, ctx):
        url_image = "https://media1.giphy.com/media/oTjoawKEq3wYD5fKEh/giphy.gif?cid=790b761175ee50ca573bd0a2605fd1598ac950fdc4a66c3c&rid=giphy.gif&ct=g"
        embed = discord.Embed(title="Kamehamerra", description="Um lazer azul feito de energia do usuario", color=0x0000f0)

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="Ki do Uzun", icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(name="Emana energia em forma de raio ", value="Um raio obliterador", inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(kamehameha(bot))