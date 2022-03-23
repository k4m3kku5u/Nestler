from discord import app_commands, Interaction
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
    
    @app_commands.command(name="ban", description="Banishes the offender permanently from the guild.")
    @app_commands.guilds(919846932459974686)
    async def ban(self, interaction: Interaction):
        if interaction.guild.owner():
            await interaction.guild.ban(user=member)
        elif interaction.user.get_role(953018980522672148):
            await interaction.guild.ban(user=member)
        else:
            await interaction.response.send_message('Insufficient role!')
   
async def setup(client):
    await client.add_cog(moderation(client))
