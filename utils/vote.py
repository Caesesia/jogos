import asyncio
import discord
import json

with open("data/scenes.json", "r", encoding="utf-8") as f:
    scenes = json.load(f)

votes = []
voters = set()

async def vote(bot, message):
    
    global votes, voters, scenes
    
    reponse = message.content.strip().upper()
    action = "poursuivre" if reponse == "O" else "arrêter"

    if message.author.id in voters:
        await message.channel.send(f"<@{message.author.id}>, tu as déjà voté.")
        return
    
    await message.channel.send(f"{message.author.name} souhaite {action}.")
    voters.add(message.author.id)
    votes.append(reponse)
 
    await asyncio.sleep(10)

    if votes.count("O") > votes.count("N"):
        await message.channel.send(f"✅ La majorité souhaite **{action}** !")
        embed_next = discord.Embed(
                title = "Clairière",
                description = scenes["scenes"][0]["desc"],
                color = discord.Color.green()
        )
        await message.channel.send(embed = embed_next)
        return

    elif votes.count("O") < votes.count("N"):
        await message.channel.send(f"🛑 La majorité souhaite **{action}**.")
        await bot.close()

    else:
        await message.channel.send("🤔 Égalité ! Le jeu **continue** par défaut.")
        await message.channel.send(embed = embed_next)
        return

    votes.clear()
    voters.clear()
