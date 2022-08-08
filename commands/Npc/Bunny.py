from discord.ext import commands
import discord


class Bunny(commands.Cog):
    """LOJAS"""
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="Bunny")
    async def embed_loja(self, ctx):
        url_image = "https://i.pinimg.com/564x/b6/b5/0b/b6b50baf07154a0f31986329acc73a32.jpg"
        embed = discord.Embed(
            title="Vendedora ambulante de livros ",
            description="Os Melhores Grimorios Que Puder Pagar",
            color=0x808080)

        embed.set_author(
            name=self.bot.user.name,
            icon_url=self.bot.user.avatar_url)
        embed.set_footer(
            text="Loja de Livros Da Bunny",
            icon_url=self.bot.user.avatar_url)

        embed.set_image(url=url_image)

        embed.add_field(
            name="Inventario",
            value="livros")
        embed.add_field(
            name="Grimorios",
            value="Livros de magias comuns",
            inline=False)
        embed.add_field(
            name="Necronomicons",
            value="Livros de magia dos mortos",
            inline=False)
        embed.add_field(
            name="Guias de sobrevienvicia",
            value="Livros que contam truques e segredos sobre ambientes",
            inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Bunny(bot))
