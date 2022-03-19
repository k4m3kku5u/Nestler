from utils.config import COGS
from discord import *
from discord.ext import commands
from dotenv import load_dotenv

client = commands.Bot(command_prefix=":")
token = load_env("CLIENT_TOKEN")
intents = Intents().default()
intents.all()

async def init():
    async with client:
        for ext in COGS:
            await client.load_extension(ext)
        await client.start(token)

@client.event
async def on_ready():
    await client.change_presence(activity=Activity(type=ActivityType.watching, name="over the nests!"))
    await client.tree.sync(guild=Object(id=919846932459974686))
