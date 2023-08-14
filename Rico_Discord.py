from discord.ext import commands
from Rico_Selenium import open_search_tokped
import asyncio
import discord
 
token = 'NTMyNDU0MjgwOTgwODU2ODMz.G3piyn.W_n7TKamdru1WaTRfvdmR0Ahl7en7FuVse5dlw'

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Hellow Guys')

@bot.command()
async def search(ctx, search):
    await open_search_tokped(search)

bot.run(token)