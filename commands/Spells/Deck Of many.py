from discord.ext import commands
import discord
import random
class deckofmany(commands.Cog):
    """deckofmany"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Deck")
    async def Deckofmany(self,ctx):
        Effect = random.randint(1, 8)
        if Effect == 1:
            url_image = "https://i.pinimg.com/originals/d4/b0/45/d4b045859ecc3a7e076b2578d9e54fff.gif"
            embed = discord.Embed(title="Carta Sol", description="Bola de fogo", color=0xff0000)

            embed.set_author(name= self.bot.user.name, icon_url= self.bot.user.avatar_url)
            embed.set_footer(text="Magia do Kozaki", icon_url= self.bot.user.avatar_url)

            embed.set_image(url=url_image)

            embed.add_field(name="Bola De Fogo", value="1d20 de dano em area", inline=True)
            await ctx.send(embed=embed)
        elif Effect == 2:
            url_image = "https://i.pinimg.com/originals/d7/17/b8/d717b8d273e64c7877216e31c4a8e00a.gif"
            embed = discord.Embed(title="Carta Polvo", description="Tentaculos de sombra", color=0xff0000)

            embed.set_author(name= self.bot.user.name, icon_url= self.bot.user.avatar_url)
            embed.set_footer(text="Magia do Kozaki", icon_url= self.bot.user.avatar_url)

            embed.set_image(url=url_image)

            embed.add_field(name="Tentaculos sombra", value="1d20 de dano na party", inline=True)
            await ctx.send(embed=embed)
        elif Effect == 3:
            url_image = "https://i.pinimg.com/originals/dc/e9/a6/dce9a67933a08c40e3fe241093bb2f8f.gif"
            embed = discord.Embed(title="Carta Relogio", description="Tempo parado", color=0xff0000)

            embed.set_author(name= self.bot.user.name, icon_url= self.bot.user.avatar_url)
            embed.set_footer(text="Magia do Kozaki", icon_url= self.bot.user.avatar_url)

            embed.set_image(url=url_image)

            embed.add_field(name="Tempo para", value="Desvia dos golpes e torna o seus indisviaveis", inline=True)
            await ctx.send(embed=embed)
        elif Effect == 4:
            url_image = "https://c.tenor.com/vVMZPUYP59IAAAAC/dnd-spell.gif"
            embed = discord.Embed(title="Todos riem Estremamente auto", description="Impossivel rodar Velocidade", color=0xff0000)

            embed.set_author(name= self.bot.user.name, icon_url= self.bot.user.avatar_url)
            embed.set_footer(text="Magia do Kozaki", icon_url= self.bot.user.avatar_url)

            embed.set_image(url=url_image)

            embed.add_field(name="risadas para todos", value="Todos riem e denucian sua posiçao", inline=True)
            await ctx.send(embed=embed)
        elif Effect == 5:
            url_image = "https://c.tenor.com/98El4k9h0BMAAAAC/counterspell.gif"
            embed = discord.Embed(title="O destroi feitiço", description="Nega proximo feitiço", color=0xff0000)

            embed.set_author(name= self.bot.user.name, icon_url= self.bot.user.avatar_url)
            embed.set_footer(text="Magia do Kozaki", icon_url= self.bot.user.avatar_url)

            embed.set_image(url=url_image)

            embed.add_field(name="Nao no seu turno", value="Nega Magia", inline=True)
            await ctx.send(embed=embed)
        elif Effect == 6:
            url_image = "https://c.tenor.com/P9lTMsSjqnMAAAAC/dnd-spell.gif"
            embed = discord.Embed(title="Luz se torna parte de um objeto a sua escolha", description="Ilumina e denuncia posição", color=0xff0000)

            embed.set_author(name= self.bot.user.name, icon_url= self.bot.user.avatar_url)
            embed.set_footer(text="Magia do Kozaki", icon_url= self.bot.user.avatar_url)

            embed.set_image(url=url_image)

            embed.add_field(name="Ilumine-se", value="adciona luz a algo e ou alguem", inline=True)
            await ctx.send(embed=embed)
        elif Effect == 7:
            url_image = "https://c.tenor.com/7vWch0UipfoAAAAC/enlarge-reduce-spell.gif"
            embed = discord.Embed(title="Aumenta o tamanho de criaturas pequenas", description="Aumenta o tamanho de insetos permanentemente", color=0xff0000)

            embed.set_author(name= self.bot.user.name, icon_url= self.bot.user.avatar_url)
            embed.set_footer(text="Magia do Kozaki", icon_url= self.bot.user.avatar_url)

            embed.set_image(url=url_image)

            embed.add_field(name="Aumenta o tamanho do seu amiguinho", value="Faz criaturas pequenas crescerem", inline=True)
            await ctx.send(embed=embed)
        elif Effect == 8:
            url_image = "https://c.tenor.com/XTRORFaKdk8AAAAC/rpg.gif"
            embed = discord.Embed(title="Invoca demonios do inferno ", description="Demonios matan coisas proximas a arrastam para o inferno", color=0xff0000)

            embed.set_author(name= self.bot.user.name, icon_url= self.bot.user.avatar_url)
            embed.set_footer(text="Magia do Kozaki", icon_url= self.bot.user.avatar_url)

            embed.set_image(url=url_image)

            embed.add_field(name="Chama ate 3 demonios", value="Ele so querem sua alma nada demais", inline=True)
            await ctx.send(embed=embed)
        elif Effect == 8:
            url_image = "https://c.tenor.com/XTRORFaKdk8AAAAC/rpg.gif"
            embed = discord.Embed(title="Invoca demonios do inferno ", description="Demonios matan coisas proximas a arrastam para o inferno", color=0xff0000)

            embed.set_author(name= self.bot.user.name, icon_url= self.bot.user.avatar_url)
            embed.set_footer(text="Magia do Kozaki", icon_url= self.bot.user.avatar_url)

            embed.set_image(url=url_image)

            embed.add_field(name="Chama ate 3 demonios", value="Ele so querem sua alma nada demais", inline=True)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(deckofmany(bot))