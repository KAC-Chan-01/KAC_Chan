import discord
from discord.ui import Select, View
from discord import app_commands, SelectOption
from discord.ext import commands
from discord.utils import get


class Roles(View):
    def __init__(self):
        super().__init__(timeout=None)
        select = Select(custom_id="select_roles", placeholder="Select Roles down here", min_values=0, max_values=4, options=[
            SelectOption(label="Updates",value='1', description="No more @everyone pings. Choose role for updates.",    emoji="🙂"),
            SelectOption(label="Games",  value='2', description="For games channel access and game notifications.", emoji="🎮"),
            SelectOption(label="Waifu",  value='3', description="Harem Collector notifications.", emoji="💗"),
            SelectOption(label="Paimon", value='4', description="Hoyoverse pings, gift codes, updates.",    emoji="🔱")
        ])
        select.callback = self.dropdown_callback
        self.add_item(select)

    async def dropdown_callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        full_set = {'1', '2', '3', '4'}
        present_set = set(interaction.data["values"])
        missing_set = full_set - present_set

        for value in present_set:
            role = None
            if value == '1':
                role = get(interaction.guild.roles, name='🙂Updates')
            elif value == '2':
                role = get(interaction.guild.roles, name='🎮Games')
            elif value == '3':
                role = get(interaction.guild.roles, name='💗Waifu')
            elif value == '4':
                role = get(interaction.guild.roles, name='🍤 Paimon')

            if role:
                await interaction.user.add_roles(role)
                await interaction.followup.send(f"Role Added : {role}", ephemeral= True)

        for value in missing_set:
            role = None
            if value == '1':
                role = get(interaction.guild.roles, name='🙂Updates')
            elif value == '2':
                role = get(interaction.guild.roles, name='🎮Games')
            elif value == '3':
                role = get(interaction.guild.roles, name='💗Waifu')
            elif value == '4':
                role = get(interaction.guild.roles, name='🍤 Paimon')

            if role:
                await interaction.user.remove_roles(role)
                await interaction.followup.send(f"Role Removed : {role}", ephemeral= True)




