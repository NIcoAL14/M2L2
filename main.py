import discord
import random
from discord.ext import commands

# Configuración de Intents
intents = discord.Intents.default()
intents.message_content = True

# Inicialización del bot
bot = commands.Bot(command_prefix='$', intents=intents)

# Evento: cuando el bot está listo
@bot.event
async def on_ready():
    print(f'✅ Conectado como {bot.user}')

# Evento: responder a mensajes específicos
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "como puedo cuidar el medio ambiente" in message.content.lower():
        await message.channel.send("🌍 Puedes cuidar el medio ambiente reciclando, reutilizando objetos y reduciendo desechos.")
    await bot.process_commands(message)

# Listas de ideas, tips y retos
ideas_list = [
    "Usa botellas plásticas para hacer macetas",
    "Convierte frascos de vidrio en recipientes para guardar alimentos",
    "Haz un portalápices con latas recicladas o el tubo del papel higiénico"
]

tips = [
    "Apaga las luces cuando no las uses",
    "Usa transporte público o bicicleta",
    "Reduce el consumo de agua cerrando la llave al cepillarte"
]

retos = [
    "Hoy intenta no usar bolsas plásticas",
    "Recoge 5 botellas plásticas y llévalas a reciclar",
    "Apaga los aparatos eléctricos que no uses"
]

preguntas = {
    "¿Cuál es el gas principal responsable del efecto invernadero?": "dióxido de carbono",
    "¿Qué color de contenedor se usa para el vidrio?": "verde"
}

# Comando: saludo inicial
@bot.command()
async def hola(ctx):
    await ctx.send("👋 Hola, soy un bot ecológico. Usa:\n- `$ideas` para ideas de reciclaje\n- `$reciclar` para consejos de separación\n- `$tip` para recibir un consejo ecológico\n- `$reto` para un reto diario\n- `$quiz` para jugar trivia ecológica")

# Comando: ideas de reciclaje
@bot.command()
async def ideas(ctx):
    idea = random.choice(ideas_list)
    await ctx.send(f"♻️ Idea: {idea}")

# Comando: consejos de reciclaje
@bot.command()
async def reciclar(ctx):
    await ctx.send("Recuerda separar residuos de la siguiente forma: 🟦 Plástico, 🟩 Vidrio, 📄 Papel y 🌱 Orgánicos")

# Comando: tips ecológicos
@bot.command()
async def tip(ctx):
    consejo = random.choice(tips)
    await ctx.send(f"💡 Consejo: {consejo}")

# Comando: retos ecológicos
@bot.command()
async def reto(ctx):
    reto = random.choice(retos)
    await ctx.send(f"🔥 Tu reto ecológico de hoy es: {reto}")

# Comando: trivia ecológica
@bot.command()
async def quiz(ctx):
    pregunta, respuesta = random.choice(list(preguntas.items()))
    await ctx.send(f"❓ {pregunta}")

    def check(m):
        return m.author == ctx.author and m.content.lower() == respuesta

    try:
        msg = await bot.wait_for("message", check=check, timeout=15)
        await ctx.send("✅ ¡Correcto!")
    except:
        await ctx.send(f"⏱️ Tiempo agotado. La respuesta era: {respuesta}")

# Ejecutar el bot (reemplaza con tu token)
bot.run("TU_TOKEN_AQUI)
