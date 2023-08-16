from Rico_Discord import RicoDiscordBot
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is ready")

bot.load_extension('Rico_Discord')
bot.run('MY TOKEN')
