from discord.ext import commands
from decouple import config

bot = commands.Bot("!-")
#                    Npcs
bot.load_extension("commands.Npc.Bunny")
bot.load_extension("commands.Npc.Silf")
#                    Deuses
bot.load_extension("commands.Gods.Hermo")
bot.load_extension("commands.Gods.Merluth")
bot.load_extension("commands.Gods.Monog")
bot.load_extension("commands.Gods.Solois")
bot.load_extension("commands.Gods.Soma_Pnevma")
bot.load_extension("commands.Gods.Xaminis")
#                    Player
bot.load_extension("commands.Players.Oliver")
bot.load_extension("commands.Players.Kozaki")
bot.load_extension("commands.Players.Gabriza")
bot.load_extension("commands.Players.Jakko")
bot.load_extension("commands.Players.Son-Uzun")
bot.load_extension("commands.Players.NuivirTarvus")
bot.load_extension("commands.Players.Void")
bot.load_extension("commands.Players.Samuel")
bot.load_extension("commands.Players.Senhorastral")
#                  Spells
bot.load_extension("commands.Spells.Deck Of many")
bot.load_extension("commands.Spells.Consumir_Magia")
bot.load_extension("commands.Spells.kamehameha")
bot.load_extension("commands.Spells.Makankosappo")
bot.load_extension("commands.Spells.kienzan")


@bot.event
async def on_ready():
    print(f"Estou pronto Estou conectado como {bot.user}")

TOKEN = config("DCTOKEN")
bot.run(TOKEN)
