import discord
import os
import discordmongo
import topgg
from discord.ext import commands, tasks
from discord import Intents

async def get_prefix(client, message):
    # Gets the prefix out of the MongoDB Database
    if not message.guild.id:
        return commands.when_mentioned_or(client.DEFAULT_PREFIX)(client, message)

    # Finds the prefix
    try:
        data = await client.prefixes.find(message.guild.id)
        if not data or "prefix" not in data:
            return commands.when_mentioned_or(client.DEFAULT_PREFIX)(client, message)

        return commands.when_mentioned_or(data["prefix"])(client, message)

    except:
        return commands.when_mentioned_or(client.DEFAULT_PREFIX)(client, message)


# Defining variables
TopggToken = os.getenv("TOPGG_TOKEN")
BotToken = os.getenv("DISCORD_TOKEN")
client = commands.Bot(command_prefix=get_prefix, intents=Intents.all(), case_insensitive=True)
client.DEFAULT_PREFIX = "h!"
client.remove_command("help")
client.topgg = topgg.DBLClient(client, TopggToken)

# Events
@client.event
async def on_ready():
    print("Bot is online and without Errors!")

@tasks.loop(minutes=30)
async def update_stats():
    try:
        await client.topgg.post_guild_count()
        print("Posted!")

    # Prints the error 
    except Exception as e:
        print(f"Failed! See Traceback\n\n{e.__class__.__name__}: {e}\n\n")

