from discord.ext import commands
from Rico_Selenium import open_search_tokped
import asyncio
import discord
 
token = '#'

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Hellow Guys')

@bot.command()
async def search(ctx, search):
    await open_search_tokped(search)

bot.run(token)