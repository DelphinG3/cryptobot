import random
import discord
import asyncio
import requests
from discord import Game
from discord.ext.commands import Bot
import aiohttp
BOT_PREFIX = ("?", "!")

client = Bot(command_prefix=BOT_PREFIX)

Client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready and connected to Discord")



@client.event
async def on_ready():
    await client.change_presence(game=Game(name="очке Антона"))
    print("Logged in as " + client.user.name)



















client.run("NDg2NTM4MjcyNzI2NTgxMjQ4.DnAjqQ.4x8O-nMDT5uUB3gqlgF_6-1kqyc")
