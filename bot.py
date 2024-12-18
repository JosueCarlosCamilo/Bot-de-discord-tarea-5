import discord # Libreria de Discord
from psw import gen_pass #from permite importar otros archivos a tu código
from psw import gen_emodji
from psw import flip_coin
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready(): #comando que enciende el bot de discord
    print('Hemos iniciado sesión como {client.user}')

# Cuando el bot reciba un mensaje, ¡enviará mensajes en el mismo canal!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('¡Hola Soy un bot!')
    elif message.content.startswith('$bye'):
        await message.channel.send('adios')
    elif message.channel.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$psw'):
        await message.channel.send('aqui tienes la cintrasena = '+ gen_pass(8))
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    else:
        await message.channel.send("No puedo procesar tu código, ¡Lo siento!")

token = "PONER AQUI EL TOKEN DE TÚ BOT"

client.run(token)
