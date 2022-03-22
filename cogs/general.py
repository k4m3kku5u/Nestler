from discord import app_commands
from discord.ext import commands

class general(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

async def setup(client):
    await client.add_cog(general(client))
