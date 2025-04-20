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
        await ctx.send(f"*Synopsis...*\n")
        await asyncio.sleep(3)

        embed_synopsis = discord.Embed(
                title = "📖 La Vengeance d'Aris",
                description = self.scenes["synopsis"],
                color = discord.Color.dark_gold()
            )
        await ctx.send(embed = embed_synopsis)
        await asyncio.sleep(15)

        embed_persos = discord.Embed(
                title = "🛡️ Les Compagnons d'Aris",
                description = self.scenes["persos"],
                color = discord.Color.purple()
            )
        await ctx.send(embed = embed_persos)
        await asyncio.sleep(10)

        embed_fin = discord.Embed(
                title = "⚔️ Le Début de la Fin",
                description=self.scenes["fin"],
                color=discord.Color.red()
        )
        await ctx.send(embed = embed_fin)
        
        #await asyncio.sleep(3)
        await ctx.send("Démarrer le jeu ?")
        await asyncio.sleep(1)
        await ctx.send("(O) - Poursuivre\n(N) - Arrêt")
        #await asyncio.sleep(10)
        
#         resultat = []
#         reponse = message.content.lower()
#         resultat = resultat.append(reponse)
# 
#         if resultat.count("O") > resultat.count("N"):
#             
#             embed_next = discord.Embed(
#                     title = "*Clairière*",
#                     description = self.scenes["intro"][0]["desc"],
#             )
# 
#             await ctx.send(embed = embed_next)

# ----------------------------------------------------------------------
# AJOUTE LES COMMANDES POUR UTILISATION
# ----------------------------------------------------------------------

async def setup(bot):
    await bot.add_cog(Start(bot))
