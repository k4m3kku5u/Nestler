from discord import app_commands
from discord import Interaction
from discord.ext import commands
from utils.embeds import pingEmbed

class general(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @app_commands.command(description="Measures latency of the client.")
    @app_commands.guilds(919846932459974686)
    async def ping(self, interaction: Interaction):
        await interaction.response.send_message(embed=pingEmbed(
            "Ping/Pong Procedure",
            "Measures latency of the client.",
            0x000000,
            datetime.utcnow()
        ))

async def setup(client):
    await client.add_cog(general(client))
