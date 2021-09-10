import discord
import aiohttp
import datetime as dt
from discord import Member
from typing import Optional
from discord.ext import commands
from discord.ext.commands import cooldown


class AnimeInformationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="quote", aliases=['q', 'aq', 'animequote'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def anime_quote(self, ctx):
        """
        This command sends a random quote from a random Anime
        """
        async with aiohttp.ClientSession() as Session:
            request = await Session.get('https://animechan.vercel.app/api/random')
            AnimeQuoteJson = await request.json()
        embed = discord.Embed(title=f"Quote from {AnimeQuoteJson['anime']}", description=f"Told by {AnimeQuoteJson['character']}", color=0xED61D3)
        embed.add_field(name="Quote", value=AnimeQuoteJson['quote'])
        await ctx.send(embed=embed)
        await Session.close()

    @commands.command(name="animeavatar", aliases=['aav', 'avatars', 'pfp', 'profilepic'])
    @cooldown(1, 5, commands.BucketType.user)
    async def anime_avatar(self, ctx):
        """
        This command sens you a random picture you can use as a profile picture
        """
        async with aiohttp.ClientSession() as Session:
            request = await Session.get('https://shiro.gg/api/images/avatars')
            AnimeAvatarJson = await request.json()
        embed = discord.Embed(title=f"Here's your Avatar {ctx.message.author.display_name}", color=0xED61D3)
        embed.set_image(url=AnimeAvatarJson['url'])
        await ctx.send(embed=embed)
        await Session.close()

    @commands.command(name="fuck", aliases=["sex"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def sexual_intercourse(self, ctx, target: Optional[Member]):
        """
        Go to horny jail
        """
        await ctx.send(file=discord.File("./cogs/images/bonk.jpg"))

    @commands.command(name="anime", aliases=['animeinfo', 'ai'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def anime_information(self, ctx, Anime_Name):
        """
        This command sends detailed Information about the Anime you want
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://kitsu.io/api/edge/anime?filter[text]={Anime_Name}") as r:
                json_data = await r.json()
        embed = discord.Embed(title=json_data['data'][0]['attributes']['titles']['en_jp'], url=f"https://kitsu.io/anime/{json_data['data'][0]['id']}", description=f"{json_data['data'][0]['attributes']['synopsis']}\n\n", color=0xED61D3)
        embed.set_thumbnail(url=json_data['data'][0]['attributes']['posterImage']['original'])
        embed.add_field(name="📆 Aired", value=f"From **{json_data['data'][0]['attributes']['startDate']}** to **{json_data['data'][0]['attributes']['endDate']}**", inline=False)
        embed.add_field(name="⌛ Status", value=f"{json_data['data'][0]['attributes']['status']}\n\n", inline=True)
        embed.add_field(name="💿 Total Episodes", value=f"{json_data['data'][0]['attributes']['episodeCount']} Episodes", inline=False)
        embed.add_field(name="⌚ Average Episode Length", value=f"{json_data['data'][0]['attributes']['episodeLength']} Minutes", inline=True)
        embed.add_field(name="🕒 Total Length (Minutes)", value=f"{json_data['data'][0]['attributes']['totalLength']} Minutes\n\n", inline=True)
        embed.add_field(name="🏆 Average Rating", value=f"{json_data['data'][0]['attributes']['averageRating']}/100", inline=False)
        embed.add_field(name="✨ Popularity Rank", value=f"#{json_data['data'][0]['attributes']['popularityRank']}", inline=False)
        embed.add_field(name="💯 Rating Rank", value=f"#{json_data['data'][0]['attributes']['ratingRank']}", inline=True)
        embed.set_footer(text=f"Powered by Kitsu ©")
        embed.timestamp = dt.datetime.utcnow()
        await ctx.send(embed=embed)
        await session.close()

    @commands.command()
    @cooldown(1, 5, commands.BucketType.user)
    async def manga(self, ctx, *, Manga_Name):
        """
        This command sends detailed Information about the Manga you want
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://kitsu.io/api/edge/manga?filter[text]={Manga_Name}") as r:
                json_data = await r.json()
        embed = discord.Embed(title=json_data['data'][0]['attributes']['titles']['en_jp'], url=f"https://kitsu.io/manga/{json_data['data'][0]['id']}", description=f"{json_data['data'][0]['attributes']['synopsis']}\n\n", color=0xED61D3)
        embed.set_thumbnail(url=json_data['data'][0]['attributes']['posterImage']['original'])
        embed.add_field(name="📆 Published", value=f"From **{json_data['data'][0]['attributes']['startDate']}** to **{json_data['data'][0]['attributes']['endDate']}**", inline=False)
        embed.add_field(name="📜 SubType", value=json_data['data'][0]['attributes']['subtype'], inline=False)
        embed.add_field(name="⌛ Status", value=f"{json_data['data'][0]['attributes']['status']}", inline=False)
        embed.add_field(name="📖 Chapters", value=f"{json_data['data'][0]['attributes']['chapterCount']} Chapter(s)", inline=True)
        embed.add_field(name="📰 Total Volumes", value=f"{json_data['data'][0]['attributes']['volumeCount']} Volume(s)", inline=True)
        embed.add_field(name="🏆 Average Rating", value=f"{json_data['data'][0]['attributes']['averageRating']}/100", inline=False)
        embed.add_field(name="✨ Popularity Rank", value=f"#{json_data['data'][0]['attributes']['popularityRank']}", inline=False)
        embed.add_field(name="💯 Rating Rank", value=f"#{json_data['data'][0]['attributes']['ratingRank']}", inline=True)
        embed.set_footer(text=f"Powered by Kitsu ©")
        embed.timestamp = dt.datetime.utcnow()
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AnimeInformationCog(bot))