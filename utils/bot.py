from discord import *
from discord.ext import commands
from dotenv import load_dotenv
from utils.config import EXTENSIONS
from utils.database import db_con_check
from os import getenv

client = commands.Bot(command_prefix=":", intents=Intents.all())
load_dotenv()

async def main():
    async with client:
        for ext in EXTENSIONS:
            await client.load_extension(ext)
        await client.start(getenv("CLIENT_TOKEN"))

@client.event
async def on_ready():
    await client.change_presence(activity=Activity(type=ActivityType.watching, name="over the nests!"))
    await client.tree.sync(guild=Object(id=919846932459974686))
    await db_con_check()
