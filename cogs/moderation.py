from discord import app_commands, Interaction
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
    
    @app_commands.command(name="ban", description="Banishes the offender permanently from the guild.")
    @app_commands.guilds(919846932459974686)
    async def ban(self, interaction: Interaction, member: Member, *, reason: str):
        embed = banEmbed()
        channel = interaction.guild.get_channel(956321900123021432)
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/919847648758992927/953452806872911892/the_nest.jpg")
        embed.add_field(name="Offender Name,", value=member.name, inline=False)
        embed.add_field(name="Offender ID,", value=member.id, inline=False)
        embed.add_field(name="Ban Reason,", value=f'{reason}', inline=False)
        
        if interaction.guild.owner():
            await interaction.guild.ban(user=member)
            await interaction.response.send_message=('Ban information was sent to the staff logs!')
            await chanel.send(embed=embed)
        elif interaction.user.get_role(953018980522672148):
            await interaction.guild.ban(user=member)
            await interaction.response.send_message=('Ban information was sent to the staff logs!')
            await channel.send(embed=embed)
        else:
            await interaction.response.send_message('Insufficient role!')
   
async def setup(client):
    await client.add_cog(moderation(client))
