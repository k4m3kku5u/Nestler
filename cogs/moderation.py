from discord import app_commands
from discord import Interaction
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @app_commands.command(description="Removes user from the guild.")
    @app_commands.guilds(919846932459974686)
    async def ban(self, interaction: Interaction):
        await interaction.response.send_message("Command is not working.")

async def setup(client):
    await client.add_cog(moderation(client=client))
