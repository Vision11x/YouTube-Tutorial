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
    if ctx.author.id == vision_id:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f"Loaded {extension} Successfully")
    else:
        return

@client.command()   
async def unload(ctx, extension):
    vision_id = 880846666624811088
    if ctx.author.id == vision_id:
        client.unload_extension(f'cogs.{extension}')    
        await ctx.send(f"Unloaded {extension} Successfully")
    else:
        return

@client.command()
async def reload(ctx, extension):
    vision_id = 880846666624811088
    if ctx.author.id == vision_id:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f"Reloaded {extension} Successfully")
    else:
        return

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("your token")
