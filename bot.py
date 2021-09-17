import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = commands.when_mentioned_or('-'), intents = discord.Intents.all())

@client.event
async def on_ready():
    print("Ready")

@client.command()
async def load(ctx, extension):
    vision_id = 880846666624811088
    if ctx.author == vision_id:
        client.load_extension(f"{extension}")
        await ctx.send(f"Loaded {extension}")
    else:
        return

@client.command()
async def unload(ctx, extension):
    vision_id = 880846666624811088
    if ctx.author == vision_id:
        client.unload_extension(f"{extension}")
        await ctx.send(f"unloaded {extension}")
    else:
        return

@client.command()
async def reload(ctx, extension):
    vision_id = 880846666624811088
    if ctx.author == vision_id:
        client.unload_extension(f"{extension}")
        client.load_extension(f"{extension}")
        await ctx.send(f"reloaded {extension}")
    else:
        return

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("ODg4MzIyODk5MjgxMzMwMTg2.YURBKw.DO92_i1bNFQadkOVK02eCwjRfUQ")