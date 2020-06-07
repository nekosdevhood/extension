from discord.ext import commands

bot = commands.Bot(command_prefix='kn!')

bot.remove_command('help')

class ExtensionClass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(ExtensionClass(bot))
