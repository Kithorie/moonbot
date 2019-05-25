import discord 
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import requests
import json
import os

print(discord.__version__) #verificando versao do discord.py

##################################
## Variáveis                    ##
##################################
description = 'Bot feito sob medida para o servidor da Lua de Gato'
token = 'NTQ0NTI4NjU0Mjc3ODA0MDQ3.XMC0BQ.cw4LUoeGNSWNjkhWngqaA9oK4iA'
bot = discord.ext.commands.Bot(command_prefix='>>')
client = discord.Client()
#Fim das variaveis

@bot.event
async def on_ready():
    print("Carregando Moon...")
    game = discord.Game("fofuras ao vento")
    await bot.change_presence(status=discord.Status.online, activity=game)

#@bot.event
#async def on_message(message):
    #if message.content.startswith('cimacimabaixobaixoesquerdadireitaesquerdadireitabastart'):
       #await message.channel.send('você destravou um novo comando!')

@bot.command()
async def ola(ctx):
    '''dê oi ao Moon!'''
    usuario = ('{}'.format(ctx.author.mention)) 
    apresentacao = 'Olá '
    continuacao = 'sou Moon, e estou pronto para o serviço!'
    await ctx.send(apresentacao + usuario + '! ' + continuacao, file=discord.File('hello.png'))

@bot.command()
async def boop(ctx):
    '''jogue o comando e veja o que o Moon irá reagir!'''
    respostas = ['meow meow~', 'boop!', 'rawr rawr~', 'purr~', '*o bot está animado com o seu comando!', '*sons de bot feliz*']
    embed=discord.Embed(description="owwwwwwn.".join(random.choices(respostas)))
    embed.set_image(url='https://i.imgur.com/HKTYDr8.png')
    await ctx.send(embed=embed)

#TODO: fazer ele ficar automatizado
@bot.command()
async def boasvindas(ctx, member: discord.Member):
    '''Este comando serve para dar boas vindas ao novo membro.'''
    users = ('{}'.format(member.mention))
    await ctx.send('Olá e seja muito bem vindo ' + users + ' ao Reino dos Gatos!' '\n' 'Leia as regras deste servidor!' '\n' 'Para mais informações leia o manual!', file=discord.File('ola.png'))


@bot.command() #o bot quem dará o abraço.
async def abraco(ctx, member: discord.Member):
    '''Irá dar um abraço na pessoa que você marcar!'''
    embed=discord.Embed(title="Você ganhou um abraço!", description="Doce doce longo abraço =w=", color=0x008080)
    embed.set_image(url='https://i.imgur.com/AYlbbmX.gif')
    users = ('{}'.format(ctx.author.mention)) 
    resposta = ' lhe deu um abraço bem apertado, '
    mencionado = ('{}'.format(member.mention))
    await ctx.send(users + resposta + mencionado + '!', embed=embed)


@bot.command() 
async def tapa(ctx, member: discord.Member):
    '''Irá dar um tapa bem forte na pessoa que você marcar!'''
    embed=discord.Embed(title="Você mereceu um tapa!", description="Realmente mereceu.", color=0x008080)
    embed.set_image(url='https://i.kym-cdn.com/photos/images/original/001/264/655/379.gif')
    users = ('{}'.format(ctx.author.mention)) 
    resposta = ' lhe deu um forte tapa, '
    mencionado = ('{}'.format(member.mention))
    await ctx.send(users + resposta + mencionado + '!', embed=embed)

@bot.command() 
async def carinho(ctx, member: discord.Member):
    '''Um momento de carinho entre você e a pessoa que marcou.'''
    embed=discord.Embed(title="Carinho time", description="owwwwwwn.", color=0x008080)
    embed.set_image(url='https://media.tenor.com/images/aab83bd3725feeaccb9929f8ca964db9/tenor.gif')
    users = ('{}'.format(ctx.author.mention)) 
    resposta = ' está lhe dando carinho, '
    mencionado = ('{}'.format(member.mention))
    await ctx.send(users + resposta + mencionado + '!', embed=embed)

@bot.command()
async def e621(ctx, *, t:str): #comando criado com sucesso.
    '''Comando feito para buscar imagens do E621'''
    tags = t.replace(" ", "%20")
    headerstype = { "User-Agent":'moon/1.0 by Luna',
    "Content-Type":"application/json", }

    response = requests.get('https://e621.net/post/index.json?&tags={}'.format(tags), headers=headerstype)
    working = json.loads(response.text)
    limite = 74
    afterwork = working[random.randint(0, limite)].get('file_url')
    catching = working[random.randint(0, limite)].get('id')
    links = 'https://e621.net/post/show/'

    embed = discord.Embed(title = "Aqui está a imagem que me pediu!", description = "beep boop", color = 0x5810ea)
    embed.set_image(url = afterwork)
    embed.set_footer(text = 'Comando E621 feito com carinho')
    if ctx.channel.is_nsfw():
        await ctx.send(links + str(catching), embed = embed)
    else:
        await ctx.send('Este não é um canal **NSFW**, taokey?')

@bot.command()
async def lab(ctx): #este comando pega uma imagem random do PC, porém, não funciona direito.
    '''Lab: pega imagens do computador NSFW e joga para você'''
    imagepath = random.choice(os.listdir('/images'))

    #embed = discord.Embed(title = 'OWO', description = 'owo')
    #embed.set_image(url=imagepath)
    #embed = discord.Embed(title = "Another command", description = "beep boop", color = 0x5810ea)
    file = discord.File('/images/'+ imagepath)
    if ctx.channel.is_nsfw():
        await ctx.send(file = file)
    else:
        await ctx.send("este não é um canal NSFW. Por favor, tente novamente.")

@bot.command()
async def gato(ctx):
    '''um comando de gatos!'''
    url = 'https://aws.random.cat/meow'
    meowurl = requests.get(url, headers = {'User-Agent': 'Moon/2'})
    data = meowurl.json()['file']

    embed = discord.Embed(title = "Um gato para você!", description = "beep boop", color = 0x5810ea)
    embed.set_image(url = data)
    embed.set_footer(text = 'alimentado pelo random.cat')

    await ctx.send(embed = embed)

#bot.command()
async def tob(ctx):
    '''o que você é? top ou bottom?'''
    variaveis = ['bottom', 'top', 'flex']
    zarolho = random.choices(variaveis)
    linkstop = ['https://static1.e621.net/data/9b/36/9b36a6406793b6f742550d1d085f6b44.jpg',
    'https://static1.e621.net/data/42/13/42139611a50cca5d3a17b90eb2132494.jpg',
    'https://static1.e621.net/data/2f/35/2f35a9ad7fa52d818d46487aa2d90ba9.png']
    linksbottom = ['https://static1.e621.net/data/47/21/4721b6736b7d8cab344cb90dab99ad55.jpg','https://static1.e621.net/data/9a/8f/9a8f74117e7898792c86235107161625.png', 'https://static1.e621.net/data/9a/8f/9a8f74117e7898792c86235107161625.png', 'https://static1.e621.net/data/cc/db/ccdbe9f13c2ac91173af9283c5dd6751.png']
    if 'bottom' in zarolho:
        afterwork = random.choices(linksbottom)
        #users = ('{}'.format(ctx.author.mention)) 
        #resposta = ' você é **bottom!**'
        embed=discord.Embed(title="TEST", description="REV1", color=0x008080)
        embed.set_image(url = afterwork)
        embed.set_footer(text = 'Dominado pelo mais forte.')
        await ctx.send (str(embed = embed))
    if 'top' in zarolho:
        await ctx.send ('2 BOT')
    if 'flex' in zarolho:
        await ctx.send ('3 BOT')

bot.run(token) 