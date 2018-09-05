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



@client.command(pass_context=True)
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await client.send_message(ctx.message.channel, "Bitcoin price is: $" + value)



















client.run("NDg2NTM4MjcyNzI2NTgxMjQ4.DnAjqQ.4x8O-nMDT5uUB3gqlgF_6-1kqyc")
