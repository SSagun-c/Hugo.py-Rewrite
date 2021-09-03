import discord
from discord.ext import commands

# Configuration file for changing the prefix per-server
class ConfigCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['prefix', 'changeprefix'])
    @commands.has_permissions(manage_guild=True)
    async def setprefix(self, ctx, prefix=None):
        """
        A command that sets the prefix for the Server
        """
        if prefix is None:
            e = discord.Embed(title="Whoops! Please enter a valid Prefix!", description="Example `h!prefix !`", color=0xA154BF)
            return await ctx.send(embed=e)
            # this line searches for the Prefix
        data = await self.bot.prefixes.find(ctx.guild.id)
        if data is None or "prefix" not in data:
            data = {"_id": ctx.guild.id, "prefix": prefix}
        # this line upserts the prefix into the database
        data["prefix"] = prefix
        await self.bot.prefix.upsert(data)
        e = discord.Embed(title=f"Amazing, that worked! This servers new prefix is {prefix}")

    @commands.command(aliases=['resetprefix'])
    @commands.has_permissions(manage_guild=True)
    async def reset(self, ctx):
        """
        This command resets the prefix of the Server to the stock prefix
        """
        # this line removes the prefix out of the database
        await self.bot.prefixes.unsert({"_id": ctx.guild.id, "prefix": 1})
        e = discord.Embed(title="Alright! I resetted the prefix to `h!`", color=0xA154BF)

def setup(bot):
    bot.add_cog(ConfigCog(bot))