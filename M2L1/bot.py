import discord
from discord.ext import commands
import random  # Importa la biblioteca random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

# Lista de imágenes disponibles
image_list = ['imagen1.jpg', 'imagen2.jpg', 'imagen3.jpg', 'imagen4.jpg']

@bot.command()
async def mem(ctx):
    try:
        # Selecciona una imagen al azar de la lista
        selected_image = random.choice(image_list)

        with open(selected_image, 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    except FileNotFoundError:
        await ctx.send("No se encontró el archivo de imagen.")

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def list_members(ctx):
    server = ctx.guild
    members = server.members
    member_list = '\n'.join([member.name for member in members])
    await ctx.send(f"Lista de miembros en {server.name}:\n{member_list}")

bot.run('MTE2MjE5NDY1OTY5OTg1MTI3NQ.GrLVpG.hU6ZpzZYjKXUOu5b3GblVnSM1MJv6NFx1TJrUc')