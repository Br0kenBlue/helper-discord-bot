import discord
from discord.ext import commands
import logging
import os
import webserver

token=os.environ['BOT_TOKEN']


handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Ready {bot.user.name}")
    try:
        guild = discord.Object(id=1093870212530585652)
        synced = await bot.tree.sync(guild=guild)
        print(f'Synced {len(synced)} commands to the guild {guild.id}')
    except Exception as e:
        print(f'Errro syncing commands: {e}')

@bot.event
async def on_member_join(member):
    await member.send(f"welcome to the server {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.lower() == 'hi':
        await message.channel.send(f"Hi {message.author.mention}")

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx.author.mention}!")

@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="New Poll", description=question)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("🍕")
    await poll_message.add_reaction("🍔")

#1093870212530585652

GUILD_ID = discord.Object(id=1093870212530585652)

'''@bot.tree.command(name="wax", description="Calculate your wax metrics", guild=GUILD_ID)
async def wax_metric(interaction: discord.Interaction):
    await interaction.response.send_message("wax is here!")'''

@bot.tree.command(name="wax", description="wax used * % /fragrance = fragrance oil", guild=GUILD_ID)
async def waxMetric(interaction: discord.Interaction, fragrance_percentage: int, fragrance_oil: int):
    await interaction.response.send_message(f"Wax ={fragrance_oil*100/fragrance_percentage}gm for fragrance % = {fragrance_percentage} and fragrance oil = {fragrance_oil}.")

@bot.tree.command(name="fragrance_percentage", description="wax used * % /fragrance = fragrance oil", guild=GUILD_ID)
async def fragP(interaction: discord.Interaction, wax: int, fragrance_oil: int):
    await interaction.response.send_message(f"Fragrance Percentage ={fragrance_oil*100/wax}% for wax = {wax} and fragrance oil = {fragrance_oil}.")

@bot.tree.command(name="fragrance_oil", description="wax used * % /fragrance = fragrance oil", guild=GUILD_ID)
async def fragOil(interaction: discord.Interaction, fragrance_percentage: int, wax: int):
    await interaction.response.send_message(f"Fragrance Oil ={wax*fragrance_percentage/100}ml for wax = {wax} and fragrance % = {fragrance_percentage}.")

webserver.keep_alive()
bot.run(token=token, log_handler=handler, log_level=logging.DEBUG)
