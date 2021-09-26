import discord
import datetime as dt
from discord.ext import commands
from discord.ext.commands.help import HelpCommand

class InformationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help_command(self, ctx):
        """This command shows a list with all commands"""
        reddit_emote = '<:reddit:872393789761781780>'
        embed = discord.Embed(title="My command list", color=0xED61D3)
        fields = [
            '🎈 Misc Commands', "`ping` | `8ball` | `pussy` | `serverinfo` | `roll` | `support` | `kill` | `invite` | `repeat` | `avatar` | `userinfo` | `wallpaper` | `botinfo` | `wouldyourather` | `weather <city>`", False, 
            '📸 Image Manipulation', "`simp` | `license` | `unoreverse", False,
            '🎭 Roleplay Commands', "`kiss` | `cry` | `hug` | `poke` | `lick` | `pat` | `nom` | `pout` | `punch` | `slap` | `blush` | `smug` | `sleep` | `tickle`", False,
            '🖋 Anime Commands', "`waifu` | `neko` | `animeweb` | `anime <Anime Name>` | `manga <Manga Name>`", False,
            '🔞 NSFW Commands', "`hentai` | `trap` | `thighs` | `boobs` | `yuri` | `bondage` | `bdsm` | `ass` | `cum` | `tentacles` | `blowjob` | `masturbation` | `ero` | `ahegao` | `uniform`", False,
            f'{reddit_emote} Reddit Command', "`reddit <your subreddit here>`", False
        ]
        for name, value, inline in fields:
            embed.add_field(name, value, inline)
        embed.timestamp = dt.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.message.author}")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(InformationCog(bot))