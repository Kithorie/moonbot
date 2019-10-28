import discord 
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import requests
import json
import os
from discord.ext.commands import has_permissions, MissingPermissions

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
    game = discord.Game("Nas Nuvens!")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("Alimentado por Luna Development Studio")

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

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(530155132449587213) #mensagem irá direto pra sala_principal
    usuario = ('{}'.format(member.mention))
    await channel.send('boas vindas, ' + usuario + '!' '\n' 'Esperamos que você tenha uma boa estadia em nosso servidor.' '\n' 'Por favor, leia as regras com atenção!' '\n''Para mais informações, leia o manual!' '\n' 'Se veio pelo Bearstars, dá uma passada no canal Anime!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(605496878779465728) #mensagem irá direto pro saida
    username = ('{}'.format(member.display_name))
    await channel.send ('O usuario ' + username + ' **saiu do servidor**')

@bot.command() #o bot quem dará o abraço.
async def abraco(ctx, member: discord.Member):
    '''Irá dar um abraço na pessoa que você marcar!'''
    abracos = ['https://static1.e621.net/data/94/cb/94cba35f18ab88704b3f778fb69ed4e0.gif',
    'https://i.imgur.com/AYlbbmX.gif',
    'https://static1.e621.net/data/ca/28/ca289ba459d138a511f216a31bfa01a2.gif',
    'https://static1.e621.net/data/39/85/39852e359d2336f2452e1bf29800c957.gif',
    'https://static1.e621.net/data/3b/c5/3bc5d46f7ed50ce6fd2af6fedc420c18.gif',
    'https://static1.e621.net/data/e8/0c/e80c8a4656a6377d08ace0a3abdd2c59.gif',
    'https://static1.e621.net/data/29/44/29444f19e32bbb14cfa54e6c7b9453ef.gif',
    'https://i.pinimg.com/originals/02/7e/0a/027e0ab608f8b84a25b2d2b1d223edec.gif'
    'https://media.giphy.com/media/13YrHUvPzUUmkM/giphy.gif'
    'https://thumbs.gfycat.com/AlienatedUnawareArcherfish-size_restricted.gif',
    'https://data.whicdn.com/images/280782407/original.gif',
    'https://media1.tenor.com/images/3264bcc47ee47ebbdd441f9f1d203542/tenor.gif',
    ]
    remix = random.choice(abracos)
    embed=discord.Embed(title="Você ganhou um abraço!", description="Doce doce longo abraço =w=", color=0x00bfff)
    embed.set_image(url= remix)
    users = ('{}'.format(ctx.author.mention)) 
    resposta = ' lhe deu um abraço bem apertado, '
    mencionado = ('{}'.format(member.mention))
    await ctx.send(users + resposta + mencionado + '!', embed=embed)


@bot.command() 
async def tapa(ctx, member: discord.Member):
    '''Irá dar um tapa bem forte na pessoa que você marcar!'''
    tapas = ['https://media.giphy.com/media/jLeyZWgtwgr2U/giphy.gif',
    'https://static1.e621.net/data/f8/fe/f8fe7c1066d2015cada6ca9b1ecf7897.jpg',
    'https://static1.e621.net/data/05/2c/052cd0ce45fa4c02efaaa3ff2efb5850.png',
    'https://static1.e621.net/data/35/f1/35f1dcf1f336b9a09ef93fc4e8923433.jpg',
    'https://static1.e621.net/data/fb/75/fb75e733d7147cbbad7d52aad6b926ec.png',
    'https://static1.e621.net/data/3f/24/3f2404458798451ff52a237d898c587f.png',
    'https://static1.e621.net/data/08/ee/08ee0830447fd2c551b73cd3a512fab0.png',
    'https://thumbs.gfycat.com/FlatAmazingFirecrest-size_restricted.gif',
    'https://media.giphy.com/media/9U5J7JpaYBr68/giphy.gif'
    'https://thumbs.gfycat.com/OblongFickleGarpike-size_restricted.gif'
    ]
    remix = random.choice(tapas)
    embed=discord.Embed(title="Você mereceu um tapa!", description="Realmente mereceu.", color=0x00bfff)
    embed.set_image(url = remix)
    users = ('{}'.format(ctx.author.mention)) 
    resposta = ' lhe deu um forte tapa, '
    mencionado = ('{}'.format(member.mention))
    await ctx.send(users + resposta + mencionado + '!', embed=embed)

@bot.command() 
async def carinho(ctx, member: discord.Member):
    '''Um momento de carinho entre você e a pessoa que marcou.'''
    cuddles = ['https://static1.e621.net/data/cf/d7/cfd71fad429db75614db190037b00aa2.gif',
    'https://static1.e621.net/data/ac/ad/acaddf9ea8b232b5dfcf68a32b87d2ec.gif',
    'https://static1.e621.net/data/a2/5d/a25d9777887ca026659a8c4eba02b7be.gif',
    'https://static1.e621.net/data/29/0b/290b0844f2337f30bcdbff4bc2f33441.gif',
    'https://media.giphy.com/media/143v0Z4767T15e/giphy.gif',
    'https://static1.e621.net/data/d1/a8/d1a85081b6324d28c8743db3fb4f2ed6.jpg',
    'https://static1.e621.net/data/0e/2a/0e2a735778fe41a8e0701aa8e706a2b6.jpg',
    ]
    remix = random.choice(cuddles)
    embed=discord.Embed(title="um momento tranquilo entre vocês dois.", description="owwwwwwn.", color=0x00bfff)
    embed.set_image(url= remix)
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

    embed = discord.Embed(title = "Aqui está a imagem que me pediu!", description = "beep boop", color = 0x00bfff)
    embed.set_image(url = afterwork)
    embed.set_footer(text = 'Comando E621 feito com carinho')
    if ctx.channel.is_nsfw():
        await ctx.send(links + str(catching), embed = embed)
    else:
        await ctx.send('Este não é um canal **NSFW**, taokey?')

@bot.command()
async def gato(ctx):
    '''um comando de gatos!'''
    url = 'https://aws.random.cat/meow'
    meowurl = requests.get(url, headers = {'User-Agent': 'Moon/2'})
    data = meowurl.json()['file']

    embed = discord.Embed(title = "Um gato para você!", description = "beep boop", color = 0x00bfff)
    embed.set_image(url = data) 
    embed.set_footer(text = 'alimentado pelo random.cat')

    await ctx.send(embed = embed)

@bot.command()
async def lambida(ctx, member: discord.Member):
    '''Isso irá com certeza lamber alguém.'''
    gifs = [
        'https://media.giphy.com/media/RQ7jEZTiuNRV6/giphy.gif', 
        'https://media.giphy.com/media/ZnnHMeC7iDSzC/giphy.gif', 
        'https://media.giphy.com/media/AdbuzBaEVJsyI/giphy.gif', 
        'https://media.giphy.com/media/3wuuNSBXnNvMs/giphy.gif', 
        'https://iruntheinternet.com/lulzdump/images/red-panda-licking-glass-window-lick-panda-14233484910.gif', 
        'https://media1.tenor.com/images/3f0f32588374adf2768b223de3503ae8/tenor.gif'
        'https://static1.e621.net/data/f0/46/f046ac7db1351f24f7820f8dce7f4270.gif'
        'https://static1.e621.net/data/1e/9b/1e9b7bbf9bd444dbd18b30e724b2e7f8.gif'
        'https://media.giphy.com/media/c6ga68AiSHowo/giphy.gif'
        'https://i.imgur.com/LA6gFPR.gif'
        'https://thumbs.gfycat.com/ThirdAngryDassie-size_restricted.gif'
        'https://www.waterdogue.com/wp-content/uploads/2017/08/why-does-your-dog-lick-you.gif'
        'https://i.pinimg.com/originals/43/ae/ae/43aeaec2f52bd1fee75c339685c1647d.gif'
        'https://cdn.discordapp.com/attachments/574463468368035841/584728030430232586/4974578.gif'
    ]
    embed = discord.Embed(title = "Você recebeu uma lambida!", description = "bleh! :P", color = 0x00bfff)
    remix = random.choice(gifs)
    embed.set_image(url = remix)
    embed.set_footer(text = 'alimentado por giphy, E621 e imgur :3')
    users = ('{}'.format(ctx.author.mention)) 
    resposta = ' está lhe dando uma lambida, '
    mencionado = ('{}'.format(member.mention))
    await ctx.send(users + resposta + mencionado, embed=embed)

@bot.command()
async def dormir(ctx):
    '''zzz...'''
    dormindo = [
        'https://static1.e621.net/data/1d/cc/1dcc48f3840f90b9230398e9aae8149a.gif',
        'https://static1.e621.net/data/3a/4f/3a4fcb8b4ed107d1ae5f6b4eee472a84.gif',
        'https://static1.e621.net/data/cd/3b/cd3b806228971ab09122e04bbc301121.gif',
        'https://static1.e621.net/data/a7/1d/a71dd746799cfaa80892a55766d3c8c4.gif',
        'https://static1.e621.net/data/e6/93/e69375c45f31beabbfef84532f2ab870.gif',
        'https://static1.e621.net/data/5d/42/5d42cb04e38eacf7be4d635f761c4b3d.gif'
    ]
    
    embed = discord.Embed(title = "Sleep Time...", description = "zzz...", color = 0x00bfff)
    remix = random.choice(dormindo)
    embed.set_image(url = remix)
    embed.set_footer(text = 'copyright a todos os artistas')
    await ctx.send(embed = embed)

@bot.command()
async def fuck(ctx, member: discord.Member):
    '''você sabe muito bem o que é isso.'''

    headerstype = { "User-Agent":'moon/1.0 by Luna', "Content-Type":"application/json", }

    response = requests.get('https://e621.net/post/index.json?&tags=male%25-2Fmale anal_penetration excessive_cum', headers=headerstype)
    working = json.loads(response.text)
    limite = 74
    afterwork = working[random.randint(0, limite)].get('file_url')
    #catching = working[random.randint(0, limite)].get('id')
    fornicacao = ['**"Mais forte! Mais fundo! Me penetre mais~"** dizia ',
    '**"Me encha mais de seu esperma~"** sussurava '
    '**Gemidos altos e ofegantes ao redor daquele ambiente, saiam da boca de**  '
    ]

    embed = discord.Embed(title = "", description = "", color = 0x00bfff)
    embed.set_image(url = afterwork)
    embed.set_footer(text = 'alimentado pelo E621')
    users = ('{}'.format(ctx.author.mention)) 
    remix = random.choice(fornicacao)
    resposta = ' enquanto é penetrado(a) incessavelmente por '
    mencionado = ('{}'.format(member.mention))
    if ctx.channel.is_nsfw():
        await ctx.send(str(remix) + mencionado + str(resposta) + users, embed = embed)
    else:
        await ctx.send('Este não é um canal **NSFW**, taokey?')

@bot.command()
async def suck(ctx, member: discord.Member):
    '''glub glub'''
    headerstype = { "User-Agent":'moon/1.0 by Luna', "Content-Type":"application/json", }

    response = requests.get('https://e621.net/post/index.json?&tags=blowjob -my_little_pony', headers=headerstype)
    working = json.loads(response.text)
    limite = 74
    afterwork = working[random.randint(0, limite)].get('file_url')
    glub = ' **chupa** '
    final = ', não desperdiçando nenhuma gota de seu **valioso e glorioso néctar.**'

    embed = discord.Embed(title = "e ambos estão aproveitando todo o momento.", description = "", color = 0x00bfff)
    embed.set_image(url = afterwork)
    users = ('{}'.format(ctx.author.mention))
    mencionado = ('{}'.format(member.mention))
    if ctx.channel.is_nsfw():
        await ctx.send(users + str(glub) + mencionado + str(final), embed = embed)
    else:
        await ctx.send('Este não é um canal **NSFW**, taokey?')

@bot.command()
async def sad(ctx):
    '''SAD CATTO'''
    
    gatinho = ['https://i.kym-cdn.com/entries/icons/original/000/026/489/crying.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/384/545/7b9.jpg',
    'https://data.whicdn.com/images/317690738/large.jpg',
    'https://i.imgur.com/jqpIP97.jpg',
    'https://66.media.tumblr.com/cda7e1958de7f8dcb34151143035a967/tumblr_pgp91sWx0N1vmskmwo4_500.jpg',
    'https://66.media.tumblr.com/af2271cc637987559c4310151e4452fd/tumblr_inline_phuxw6Zkmo1ryyjv7_500.jpg',
    'https://www.meme-arsenal.com/memes/99c8c60c91dca84f9e73cb18272db878.jpg',
    'https://data.whicdn.com/images/325778968/large.jpg',
    'https://a.wattpad.com/cover/117607376-288-k496783.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/434/447/ce8.png',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/401/645/e0b.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/400/361/ade.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/394/475/973.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/389/478/8a9.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/389/479/eca.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/389/465/663.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/475/526/f09.png',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/384/543/865.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/389/458/3af.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/389/455/496.png',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/389/464/318.png',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/389/454/ca7.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/389/434/7f5.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/389/435/d91.png',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/389/432/ef5.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/389/426/860.png',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/389/400/49a.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/389/394/332.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/384/764/a62.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/384/827/b73.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/384/532/161.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/384/550/69b.jpg',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/384/535/295.jpg',
    'https://data.whicdn.com/images/327767201/superthumb.jpg'
    ]

    remix = random.choice(gatinho)
    embed = discord.Embed(title = ";----------;", description = ";-;", color = 0x00bfff)
    embed.set_image(url = remix)
    embed.set_footer(text = ';--------;')
    await ctx.send(embed = embed)

@bot.command() #o bot quem dará o abraço.
async def beijo(ctx, member: discord.Member):
    '''Irá dar um beijo na pessoa que você marcar!'''
    abracos = ['https://media1.tenor.com/images/31362a548dc7574f80d01a42a637bc93/tenor.gif',
    'https://media1.tenor.com/images/45e529c116a1758fd09bdb27e2172eca/tenor.gif',
    'https://media1.tenor.com/images/b1189e353db0bed3521885bec284264b/tenor.gif',
    'https://media1.tenor.com/images/104b52a3be76b0e032a55df0740c0d3b/tenor.gif',
    'https://media1.tenor.com/images/ef9687b36e36605b375b4e9b0cde51db/tenor.gif',
    'https://media1.tenor.com/images/5c712c9fc3f17b1735a36b8ec65996ba/tenor.gif',
    'https://media1.tenor.com/images/185d7a67052baca9b7a9db90a321329a/tenor.gif',
    'https://media1.tenor.com/images/cddc857b201c0273452a7ceddf0acca4/tenor.gif'
    'https://media1.tenor.com/images/04c894c51f70dd24acd59ec5392a1584/tenor.gif'
    'https://media1.tenor.com/images/c4ff310ed4399ebe2c85ffc52ad5eeab/tenor.gif',
    'https://media1.tenor.com/images/a66f4ac0deded0a2a12260cb1af11c3c/tenor.gif',
    'https://media1.tenor.com/images/141cdec52c53abfebb0dece3f06f4177/tenor.gif',
    'https://media1.tenor.com/images/20afd6fa304cd271ba789c45132f6755/tenor.gif',
    'https://media1.tenor.com/images/1ec5380287a1eb3abd0faa66febeb081/tenor.gif',
    ]
    remix = random.choice(abracos)
    embed=discord.Embed(title="Você ganhou um beijo!", description="-3- mwah! mwah!", color=0x00bfff)
    embed.set_image(url= remix)
    users = ('{}'.format(ctx.author.mention)) 
    resposta = ' lhe deu um beijo, '
    mencionado = ('{}'.format(member.mention))
    await ctx.send(users + resposta + mencionado + '!', embed=embed)

@bot.command()
async def sk8(ctx):
    '''Mas ela vai voltar, mas ela vai voltar'''
    skatinho = ['https://cdn.discordapp.com/attachments/530155132449587213/620100443325988875/image0.png',
                'https://cdn130.picsart.com/294383378067211.png'
            ]
    remix = random.choice(skatinho)
    embed = discord.Embed(title = "Só os Skates sabem....", description = "Mas ela vai voltar..Mas ela vai Voltar aaaah", color = 0x00bfff)
    embed.set_image(url = remix)
    embed.set_footer(text = 'featuring lulinha')
    await ctx.send(embed=embed)

@bot.command()
@has_permissions(manage_messages=True, manage_roles=True, ban_members=True)
async def new(ctx, member: discord.Member, *, mot:str):
    '''Comando para advertências'''
    channel = bot.get_channel(638453245504651295)
    embed = discord.Embed (title = "Notificação de Advertência", description = "Esta ação foi necessária para lhe notificar que você infringiu uma regra do servidor.")
    avatar = member.avatar_url
    administrador = ctx.message.author.avatar_url
    embed.set_author(name=member.name, icon_url = avatar)
    embed.set_footer (icon_url = administrador, text = "essa ação foi feita por: {}".format(ctx.author.name))
    usuario = (' {} '.format(member.mention))
    mensagem = "O membro "
    espaco = " foi **advertido** por: "
    await channel.send (mensagem + usuario + espaco + mot, embed = embed)

bot.run(token) 