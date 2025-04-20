import asyncio
import discord
import json

with open("data/scenes.json", "r", encoding="utf-8") as f:
    scenes = json.load(f)

votes = []

async def vote(message):

    reponse = message.content.upper()
    votes.append(reponse)
    
    await asyncio.sleep(5)

    if votes.count("O") > votes.count("N"):

        embed_next = discord.Embed(
                title = "Clairière",
                description = scenes["scenes"][0]["desc"],
                color = discord.Color.green()
        )

        await message.channel.send(embed = embed_next)

    votes.clear()
