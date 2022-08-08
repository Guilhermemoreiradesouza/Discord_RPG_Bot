from discord.ext import commands
import random

class Talks(commands.Cog):
    """Send Potions"""

    def __int__(self,bot):
        self.bot = bot

        # eventos  -> commands.listener
    @commands.command()
    async def on_reaction_add(self, ctx):
        Dice=random.randint(1,10)
#              change image
def setup(bot):
    bot.add_cog(Talks(bot))

