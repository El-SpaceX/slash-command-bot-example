import discord
import json, random
from discord.ext import commands
from aioconsole import aprint



CONFIGS = json.load(open("configs.json", 'r'))

intents = discord.Intents.all()
client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    await aprint(f"Conectado com sucesso.\nUser: {client.user}\nID: {client.user.id}")



@client.slash_command(name='random')
async def randomcommand(ctx: discord.commands.ApplicationContext): 
    embed =  discord.Embed(title="Numero gerado", description=f"{random.randint(0, 100)}")
    await ctx.respond(embed=embed)

client.run(CONFIGS["TOKEN"])






