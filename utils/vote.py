import asyncio
import discord
import json

with open("data/scenes.json", "r", encoding="utf-8") as f:
    scenes = json.load(f)

votes = []
voters = set()
timer = False


async def vote(bot,  message):
    
    global votes, voters, scenes, timer

    reponse = message.content.strip().upper()
    action = "poursuivre" if reponse == "O" else "arrêter"

    if message.author.id in voters:
        await message.channel.send(f"<@{message.author.id}>, tu as déjà voté.")
        return
    
    await message.channel.send(f"{message.author.name} souhaite {action}.")
    voters.add(message.author.id)
    votes.append(reponse)

    if not timer:
        timer = True
        asyncio.create_task(result(bot, message, reponse, action))


async def result(bot, message, reponse, action):
    
    global votes, voters, scenes

    await asyncio.sleep(10)

    embed_next = discord.Embed(
            title = "Clairière",
            description = scenes["scenes"][0]["desc"],
            color = discord.Color.green()
    )
    
    await message.channel.send(f"{votes.count('O')} vote[s] pour continuer.\n"
        f"{votes.count('N')} vote[s] pour arrêter.")

    await asyncio.sleep(3)

    if votes.count("O") > votes.count("N"):
        await message.channel.send(f"✅ La majorité souhaite **{action}** !")
        await message.channel.send(embed = embed_next)

    elif votes.count("O") < votes.count("N"):
        await message.channel.send(f"🛑 La majorité souhaite **{action}**.")
        await bot.close()

    elif votes.count("O") == votes.count("N"):
        await message.channel.send("🤔 Égalité ! Le jeu **continue** par défaut.")
        await message.channel.send(embed = embed_next)
    else:
        await message.channel.send("erreur astagfirullah!!!")

    votes.clear()
    voters.clear()
