from discord import app_commands, Interaction, Member
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
    
    @app_commands.command(name="ban", description="Banishes the offender permanently from the guild.")
    @app_commands.guilds(919846932459974686)
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(self, interaction: Interaction, member: Member, *, reason: str):
        embed = banEmbed()
        channel = interaction.guild.get_channel(956321900123021432)
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/919847648758992927/953452806872911892/the_nest.jpg")
        embed.add_field(name="Offender Name,", value=member.name, inline=False)
        embed.add_field(name="Offender ID,", value=member.id, inline=False)
        embed.add_field(name="Ban Reason,", value=f'{reason}', inline=False)
        
        if member is interaction.user:
            await interaction.response.send_message("Must supply a valid parameter other than yourself!")
        elif member is interaction.guild.owner:
            await interaction.response.send_message("Nice try though! You cannot ban the guild owner.")
        else:
            await interaction.guild.ban(user=member, reason=reason)
            await interaction.response.send_message('Ban information was sent to the staff logs!')
            await channel.send(embed=embed)
        
    @app_commands.command(name="kick", description="Removes offender from the guild temporarily")
    @app_commands.guilds(919846932459974686)
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self, interaction: Interaction, member: Member, *, reason: str):
        embed = kickEmbed()
        channel = interaction.guild.get_channel(956321582823919706)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="Discord Username,", value=member.name, inline=False)
        embed.add_field(name="Discord Identifier,", value=member.id, inline=False)
        embed.add_field(name="Reason for removal,", value=reason, inline=False)

        if member is interaction.user:
            await interaction.response.send_message("Must supply a valid parameter other than yourself!")
        elif member is interaction.guild.owner:
            await interaction.response.send_message("Nice try though! You cannot ban the guild owner.")
        else:
            await interaction.guild.kick(user=member, reason=reason)
            await interaction.response.send_message("Kick information was sent to the staff logs!")
            await channel.send(embed=embed)
   
async def setup(client):
    await client.add_cog(moderation(client))
