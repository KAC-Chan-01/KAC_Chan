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
#import motor.motor_asyncio
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageColor, ImageStat
from sushii import BasicRolesButton,AnnivRolesButton, RmAnnivButton
from shu import Roles
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
        client.add_view(BasicRolesButton())
        client.add_view(AnnivRolesButton())
        client.add_view(RmAnnivButton())

    except Exception as e:
        print(e)

@client.event
async def on_guild_join(guild):
    return 0

@client.event
async def on_guild_remove(guild):
    return 0


# TEST ##########################################################################################################################################################################

@client.tree.command(name="hello", description="Simple hello command")
@app_commands.describe(your_name = "Enter your Name")
async def hello(interaction: discord.Interaction, your_name:str):
    if interaction.user.guild_permissions.administrator:    
        return await interaction.response.send_message(f"hello {your_name}", ephemeral= True)
    else:
        return await interaction.response.send_message(f"You can't use that", ephemeral= True)





# VC COMMANDS ##################################################################################################################################################################

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


@client.tree.command(name="getuserpic", description="Get's that sweet picture of an member")
@app_commands.describe(user= "Select User")
async def getuserpic(interaction: discord.Interaction, user:discord.User):
    if interaction.user.guild_permissions.administrator:
        return await interaction.response.send_message(user.avatar.url, ephemeral= False)
    else:
        return await interaction.response.send_message(f"You dont have permission for this command", ephemeral= True)


@client.tree.command(name="say", description="Say as if you're the bot")
@app_commands.describe(say="What you want to say")
@app_commands.describe(where="Where you want to say")
async def say(interaction: discord.Interaction, say: str, where: discord.TextChannel):
    if interaction.user.guild_permissions.administrator:
        await where.send(say)
        await interaction.response.send_message(f"Message sent to {where.mention}.", ephemeral=True)
    else:
        await interaction.response.send_message("Nikal beh", ephemeral=True)


@client.tree.command(name="roles", description="Get your basic roles here")
@app_commands.describe(channel="What you want to say")
async def roles(interaction: discord.Interaction, channel:discord.TextChannel):
    await interaction.response.defer(ephemeral= True)
    if interaction.user.guild_permissions.administrator:
        message = "# Basic Roles\n# ✦ Select your Roles.\n-# Please choose the roles you require from the dropdown menu below and deselect them when no longer needed.\n- Updates\n-# To accommodate everyone's preferences regarding announcements, we will discontinue the use of @everyone pings going forward. Please select this role to receive future updates.\n- Games\n-# To obtain the Games role, please select it below to unlock access to the games channel. This role will also be used to notify you about any games being played on the server.\n- Waifu\n-# You may also select this if you wish to receive notifications for Harem Collector. This will assign you a new role dedicated to updates related to those channels.\n- Paimon\n-# Select this role to receive the Paimon role, which includes Hoyoverse-related pings such as gift codes and updates."
        embed = discord.Embed(description=message, color=discord.Color(0xBD0028))
        embed.set_footer(text=f"{interaction.guild.name}", icon_url=interaction.guild.icon.url)
        await channel.send(embed=embed, view=Roles())
        return await interaction.followup.send(f"Sent")
    else:
        return await interaction.followup.send(f"Chal be lodu, apna muh me lele")


@client.tree.command(name="buttons")
async def buttons(interaction: discord.Interaction,channel:str):
    channel = client.get_channel(int(channel))
    await channel.send(content="Buttons Menu",view=BasicRolesButton())
    await interaction.response.send_message(content=f'Message sent in {channel.mention}')


@client.tree.command(name="annivbuttons")
async def annivbuttons(interaction: discord.Interaction,channel:discord.TextChannel):
    await channel.send(content=None,embed=(discord.Embed(description="# 5th Anniversary Roles\n# ✦ Select your Role.\n-# Each icon is color-coded to represent a specific role. You can have only one anniversary role at a time. Clicking on a different icon will remove your current role and assign the new one.",color=discord.Color.from_rgb(165, 52, 53))),view=AnnivRolesButton())
    await channel.send(content=None,embed=(discord.Embed(description="# ✦ Remove your Role.\n-# This will remove your anniversary role, but you can reassign yourself a role at any time.",color=discord.Color.from_rgb(165, 52, 53))),view=RmAnnivButton())
    await interaction.response.send_message(content=f'Message sent in {channel.mention}')


@client.tree.command(name="say_christmass", description="Christmass Wishes")
@app_commands.describe(where="Where you want to say")
async def say_christmass(interaction: discord.Interaction, where: discord.TextChannel):
    if interaction.user.guild_permissions.administrator:
        await where.send(f"<@&673276401037606961>\n-# <a:1PadoruPadoru:643947472070115347> \n**MERRY CHRISTMAS FROM KOLKATA ANIME CLUB**\nMay your festive spirit shine brighter than the stars, and your days be filled with laughter as pure as the first snow!\n\nFor the next 2 weeks, you can get the **Padoru** role by typing **!Padoru** in the chat.\n\n-# ✦ Also, have a look at <#1321545163813949523> when it's ready. :eyes:")
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









client.run(dotenv_values("/root/KAC_Chan/token.env")["BOT_TOKEN"])




