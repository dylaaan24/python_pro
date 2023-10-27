import discord
from discord.ext import commands

# Definir las intenciones requeridas
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)  # Incluyendo intenciones

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    channel_id = 1157005777387655178
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send('''Hola, mi nombre es botgame y soy un catálogo de videojuegos.
                           Puedes agregar juegos usando el comando !agregar_juego.''')

# Base de datos (ejemplo con su diccionario)
game_catalog = {}

# Comando para agregar un juego
@bot.command()
async def agregar_juego(ctx, titulo, plataforma, genero):
    game_catalog[titulo] = {"Plataforma": plataforma, "Género": genero}
    await ctx.send(f'Se ha agregado el juego "{titulo}" al catálogo.')

# Comando para buscar un juego
@bot.command()
async def buscar_juego(ctx, titulo):
    juego = game_catalog.get(titulo)
    if juego:
        await ctx.send(f'Juego encontrado: {titulo}\nPlataforma: {juego["Plataforma"]}\nGénero: {juego["Género"]}')
    else:
        await ctx.send(f'El juego "{titulo}" no se encuentra en el catálogo.')

# Otros comandos y funcionalidades

# Autenticación y conexión al servidor de Discord
bot.run('MTE2MjE5NDY1OTY5OTg1MTI3NQ.GuyRKt.JxNOq-CDJw7-s4gWhRpM5Gm_OFYWmrVq9YUgNA')