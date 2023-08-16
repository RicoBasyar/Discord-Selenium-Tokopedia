from discord.ext import commands

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Test Cog is ready!')

    @commands.command()
    async def test(self, ctx):
        await ctx.send('Test command works!')

def setup(bot):
    bot.add_cog(TestCog(bot))