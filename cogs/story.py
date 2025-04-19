from discord.ext import commands
import json
import discord
import asyncio


def lecture():
    with open("data/scenes.json", "r") as f:
        return json.load(f)




# ----------------------------------------------------------------------
# REGROUPE LES COMMANDES LIEES AU FONCTIONNEMENT DU BOT 
# ----------------------------------------------------------------------

class Start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.scenes = lecture()

    @commands.command(help = "Démarre le RPG")
    async def on(self, ctx):
        await ctx.send(f"*Démarrage...*\n")
        await asyncio.sleep(3)
        await ctx.send("------------------------")
        await asyncio.sleep(1)
        await ctx.send(self.scenes["synopsis"])
        await asyncio.sleep(30)
        await ctx.send("------------------------")
        await asyncio.sleep(1)
        await ctx.send(self.scenes["persos"])
        await asyncio.sleep(15)
        await ctx.send("------------------------")
        await asyncio.sleep(1)
        await ctx.send(self.scenes["fin"])



# ----------------------------------------------------------------------
# AJOUTE LES COMMANDES POUR UTILISATION
# ----------------------------------------------------------------------

async def setup(bot):
    await bot.add_cog(Start(bot))
