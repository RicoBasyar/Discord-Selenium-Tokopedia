from discord.ext import commands
from Rico_Selenium import TokopediaScraper
import asyncio
import discord

class RicoDiscordBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Hellow Guys')

    @commands.command()
    async def search(self, ctx, *,search):
        tokopedia_scraper = TokopediaScraper()
        search_result = await tokopedia_scraper.open_search_tokped(search)

        message = '**Hasil pencarian :\n**'
        for name, price in zip(range(11), search_result):
            message = message + f'`{name} - {price}`\n'

        while message:
            # Split the message into a chunk that's less than 2000 characters
            chunk, message = message[:2000], message[2000:]
            await ctx.send(chunk)
    
    @commands.command()
    async def test(self, ctx):
        await ctx.send('Bot siap lur')

def setup(bot):
    bot.add_cog(RicoDiscordBot(bot))