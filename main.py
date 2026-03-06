import discord
import random
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
#Que el usuario haga una pregunta
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "como puedo cuidar el medio ambiente" in message.content.lower():
        await message.channel.send("Puedes cuidar el medio ambiente reciclando, reutilizando objetos, reduciendo desechos")
    await bot.process_commands(message)
ideas_list = ["Usa botellas plásticas para hacer macetas", "Convierte frascos de vidrio en recipientes para guardar alimentos", "Haz un portalapices con latas recicladas o el tubo del papel higiénico"]
@bot.command()
async def hola(ctx):
    await ctx.send("Hola, soy un chat bot ecológico. Si pones $ideas, te pudo dar aleatoriamente alguna de mis ideas, si pones $reciclar, te digo la forma en la que puedes reciclar y si pones como puedo cuidar el medio ambiente, te lo puedo explicar")
@bot.command()
async def ideas(ctx):
    idea = random.choice(ideas_list)
    await ctx.send(idea)
@bot.command()
async def reciclar(ctx):
    await ctx.send("Recuerda separar residuos de la siguiente forma: plástico, vidrio, papel y orgánicos")
bot.run('TU_TOKEN_AQUI')
