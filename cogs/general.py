from datetime import datetime
from discord import app_commands, Interaction
from discord.ext import commands
from utils.embeds import pingEmbed

class general(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
    
    @app_commands.command(name="ping", description="")
    @app_commands.guilds()
    async def ping(self, interaction: Interaction)
        embed = pingEmbed()
        embed.set_author(name=f'{interaction.user.name}', icon_url=interaction.user.avatar)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/919847648758992927/953452806872911892/the_nest.jpg")
        embed.add_field(name="CLIENT,", value=f"{round(self.client.latency * 1000)}ms", inline=True)
        embed.add_field(name="DAPI,", value=None, inline=True)
        embed.set_footer(text="Brought to you by: The Nest HQ.")
        await interaction.response.send_message(embed=embed)

async def setup(client):
    await client.add_cog(general(client))
