# Copy from KAC Chan for local testing only

import aiohttp
import asyncio
from dotenv import dotenv_values
import discord
from discord.ui import Select, View
from discord import app_commands, SelectOption
from discord.ext import commands
from discord.utils import get
import io
import math
import motor.motor_asyncio
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageColor, ImageStat
import random
import re
from typing import Optional
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

intents = discord.Intents.all()
intents.voice_states = True

client = commands.Bot(command_prefix='+', activity=discord.Activity(type=discord.ActivityType.watching, name="over KAC"), intents=intents)

@client.event
async def on_ready():
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} Commands")

        client.add_view(Roles())

    except Exception as e:
        print(e)

@client.event
async def on_guild_join(guild):
    return 0

@client.event
async def on_guild_remove(guild):
    return 0

class Roles(View):
    def __init__(self):
        super().__init__(timeout=None)
        select = Select(custom_id="select_roles", placeholder="Select Roles down here", min_values=0, max_values=4, options=[
            SelectOption(label="Updates",value='1', description="Role to get Updates about upcoming announcements.",       emoji="🙂"),
            SelectOption(label="Games",  value='2', description="Role to get access to Games Channel and its Voice Chats", emoji="🎮"),
            SelectOption(label="Waifu",  value='3', description="Role to get access to Waifu Collector and its events",    emoji="💗"),
            SelectOption(label="Paimon", value='4', description="Role to get access to Genshin and Honkai Impact channels",emoji="🍤")
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

        await interaction.followup.send("Roles updated!", ephemeral=True)


# TEST ##########################################################################################################################################################################

@client.tree.command(name="hello", description="Simple hello command")
@app_commands.describe(your_name = "Enter your Name")
async def hello(interaction: discord.Interaction, your_name:str):
    return await interaction.response.send_message(f"hello {your_name}", ephemeral= True)









# UTILITY COMMANDS #############################################################################################################################################################

@client.tree.command(name="ping", description="Check Latency")
async def ping(interaction: discord.Interaction):
    return await interaction.response.send_message(f"Ping: "+str(1000 * round(client.latency,3))+"ms", ephemeral= True)


@client.tree.command(name="getuser", description="Get's Users ID")
@app_commands.describe(user= "Select User")
async def getuser(interaction: discord.Interaction, user:discord.User):
    if interaction.user.guild_permissions.administrator:
        return await interaction.response.send_message(f"Discord ID: {user.id}", ephemeral= False)
    else:
        return await interaction.response.send_message(f"You dont have permission for this command", ephemeral= True)
    
    
@client.tree.command(name="getuserpic", description="Get's Users Pic")
@app_commands.describe(user= "Select User")
async def getuserpic(interaction: discord.Interaction, user:discord.User):
    if interaction.user.guild_permissions.administrator:
        return await interaction.response.send_message(user.avatar.url, ephemeral= False)
    else:
        return await interaction.response.send_message(f"You dont have permission for this command", ephemeral= True)


@client.tree.command(name="roles", description="Get your basic roles here")
@app_commands.describe(title="Where you want to say")
@app_commands.describe(message="Where you want to say")
@app_commands.describe(channel="What you want to say")
async def roles(interaction: discord.Interaction, title:str, message:str, channel:discord.TextChannel):
    await interaction.response.defer(ephemeral= True)
    if interaction.user.guild_permissions.administrator:
        embed = discord.Embed(title=title, description=message, color=discord.Color(0xBD0028))
        await channel.send(embed=embed, view=Roles())
        return await interaction.followup.send(f"Sent")
    else:
        return await interaction.followup.send(f"Chal be lodu, apna muh me lele")


@client.tree.command(name="say", description="Play Music")
@app_commands.describe(say="What you want to say")
@app_commands.describe(where="Where you want to say")
async def say(interaction: discord.Interaction, say: str, where: discord.TextChannel):
    if interaction.user.guild_permissions.administrator:
        await where.send(say)
        await interaction.response.send_message(f"Message sent to {where.mention}.", ephemeral=True)
    else:
        await interaction.response.send_message("Nikal beh", ephemeral=True)





# GAME COMMANDS ################################################################################################################################################################

@client.tree.command(name="toss", description="Toss a coin")
async def toss(interaction: discord.Interaction):
    coin = random.randint(0, 1)
    if coin % 2 == 0:
        return await interaction.response.send_message("Heads", delete_after= 180)
    else:
        return await interaction.response.send_message("Tails", delete_after= 180)


@client.tree.command(name="join", description="Join's users voice channel")
async def join(interaction: discord.Interaction):
    if interaction.user.voice is None:
        return await interaction.response.send_message(f"You're not in a vc, cant join", ephemeral= True)
    if interaction.guild.voice_client is not None:
        return await interaction.response.send_message(f"Occupied, cant join your vc", ephemeral= True)
    if interaction.user.voice.channel is not None:
        await interaction.user.voice.channel.connect()
        return await interaction.response.send_message(f"Joining {interaction.user.voice.channel} Channel", ephemeral= False)
    

@client.tree.command(name="leave", description="Leaves's users voice channel")
async def leave(interaction: discord.Interaction):
    if interaction.guild.voice_client is None:
        return await interaction.response.send_message(f"Not connected to any vc at the moment", ephemeral= True)
    if interaction.guild.voice_client is not None:
        if interaction.user.voice is None:
            return await interaction.response.send_message(f"You're not in the vc", ephemeral= True)
        elif interaction.user.voice.channel == interaction.guild.voice_client.channel:
            await interaction.response.send_message(f"Leaving the {interaction.guild.voice_client.channel}", ephemeral= False)
            return await interaction.guild.voice_client.disconnect()
        else:
            return await interaction.response.send_message(f"You cant use this", ephemeral= True)






class BasicRolesButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Updates',row=0,custom_id="bsrbutton-1",style=discord.ButtonStyle.grey,emoji="<:KAC:821442181784010813>")
    async def but1(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(673276401037606961)
        if discord.Client.role not in interaction.user.roles:
            await interaction.user.add_roles(discord.Client.role)
            await interaction.response.send_message(f"Granted {discord.Client.role.mention} role to you", ephemeral=True, delete_after=5)
        else:
            await interaction.user.remove_roles(discord.Client.role)
            await interaction.response.send_message(f"Taken {discord.Client.role.mention} role from you", ephemeral=True, delete_after=5)

    @discord.ui.button(label='Games',row=0,custom_id="bsrbutton-2",style=discord.ButtonStyle.grey,emoji="🎮")
    async def but2(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(668556934252593152)
        if discord.Client.role not in interaction.user.roles:
            await interaction.user.add_roles(discord.Client.role)
            await interaction.response.send_message(f"Granted {discord.Client.role.mention} role to you", ephemeral=True, delete_after=5)
        else:
            await interaction.user.remove_roles(discord.Client.role)
            await interaction.response.send_message(f"Taken {discord.Client.role.mention} role from you", ephemeral=True, delete_after=5)

    @discord.ui.button(label='Waifu',row=1,custom_id="bsrbutton-3",style=discord.ButtonStyle.grey,emoji="💕")
    async def but3(self,interaction:discord.Interaction, Button:discord.ui.button):
        discord.Client.role=interaction.guild.get_role(683406500412260374)
        if discord.Client.role not in interaction.user.roles:
            await interaction.user.add_roles(discord.Client.role)
            await interaction.response.send_message(f"Granted {discord.Client.role.mention} role to you", ephemeral=True, delete_after=5)
        else:
            await interaction.user.remove_roles(discord.Client.role)
            await interaction.response.send_message(f"Taken {discord.Client.role.mention} role from you", ephemeral=True, delete_after=5)

    @discord.ui.button(label='Paimon',row=1,custom_id="bsrbutton-4",style=discord.ButtonStyle.grey,emoji="<a:1Hulalalala:758396999593754645>")
    async def but4(self,interaction:discord.Interaction, Button:discord.ui.button):
        discord.Client.role=interaction.guild.get_role(748601760813416528)
        if discord.Client.role not in interaction.user.roles:
            await interaction.user.add_roles(discord.Client.role)
            await interaction.response.send_message(f"Granted {discord.Client.role.mention} role to you", ephemeral=True, delete_after=5)
        else:
            await interaction.user.remove_roles(discord.Client.role)
            await interaction.response.send_message(f"Taken {discord.Client.role.mention} role from you", ephemeral=True, delete_after=5)

@client.tree.command(name="buttons")
async def buttons(interaction: discord.Interaction,channel:str):
    channel = client.get_channel(int(channel))
    await channel.send(content="Buttons Menu",view=BasicRolesButton())
    await interaction.response.send_message(content=f'Message sent in {channel.mention}')










client.run(dotenv_values("token.env")["BOT_TOKEN"])


#/home/shubhojit/Euphie/token.env




