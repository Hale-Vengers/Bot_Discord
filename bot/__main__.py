import datetime
import discord
import random
import time
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get
from test_cog import TestCog

load_dotenv()

bot = commands.Bot(command_prefix='$',help_command=None)

@bot.event
async def on_ready():
    print('Connected as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    owo = "owo"
    hoot = "hoot"
    hoots = "<@!382963563389648896>"
    content = message.content.lower()
    
    if message.author == bot.user:
        return
    
    if hoot in content:
        await message.channel.send(file=discord.File('medias/images/hoothoot.png'))
        
    if "owo" in content:
        await message.channel.send("Amende uwu")        

    if "uwu" in content:
        await message.channel.send("Amende owo")
    if hoots in content:
        await message.channel.send(file=discord.File('medias/images/hoothoot.png'))
        
    await bot.process_commands(message)



@bot.command()
async def help(ctx):
    await ctx.send("La commande d'aide est $aide :)")

@bot.command(pass_context=True)
async def aide(ctx):
    author= ctx.message.author
        
    embed = discord.Embed(
        colour = discord.Colour.purple(),
        title = "--- Page d'aide ---"
        )
    
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/813145774320910359/824010122581114970/received_187979142621558.jpeg?width=300&height=300")
    
    embed.add_field(name = "____________________\n------> Bonus :", value="Commandes bonus", inline = False)
    embed.add_field(name = "$aide", value = "Envoi la page que vous voyez actuellement", inline = False)
    embed.add_field(name = "$bonbot", value = "Remercie le bot pour ses loyaux services", inline = False)
    embed.add_field(name = "$dodo", value = "Souhaite une bonne nuit", inline = False)
    embed.add_field(name = "$hayato #", value = "Invoque Hayato # fois", inline = False)
    embed.add_field(name = "$icedblue", value = "Réponds à la question \"quelle est la meilleure des bières ?\"", inline = False)
    
    embed.add_field(name = "____________________\n------> Empire :", value="Commandes dédiés au rappeur EMPIRE", inline = False)
    embed.add_field(name = "$impardonnable", value = "Sors une quote de son son Impardonnable", inline = False)
    embed.add_field(name = "$lyricsimpardonnable", value = "Envoi en MP les lyrics d'Impardonnable.", inline = False)
    
    embed.add_field(name = "____________________\n------> Personnalisés :", value="Commandes dédiés aux Hale-Vengers", inline = False)
    embed.add_field(name = "$fantomas", value = "Deviens FANTOMAS", inline = False)
    embed.add_field(name = "$hale", value = "Juste Hale.", inline = False)
    embed.add_field(name = "$hoothoot #", value = "HOOT-HOOT (# = le nombre de fois ou il doit apparaître", inline = False)
    embed.add_field(name = "$raph", value = "?", inline = False)
    
    embed.add_field(name = "____________________\n------> Signes :", value="Commandes liés au système de signes", inline = False)
    embed.add_field(name = "$addsigne ######", value = "Cette commande permet d'ajouter une phrase (ici ######) dans la liste de signes.", inline = False)
    embed.add_field(name = "$listesignes", value = "Cette commande permet de lister les différentes phrases", inline = False)
    embed.add_field(name = "$donneznousunsigne", value = "Cette commande donne un signe au hasard parmi la liste.", inline = False)
    
    embed.add_field(name = "____________________\n------> Textuels :", value="Commandes dédiés au chat", inline = False)
    embed.add_field(name = "$clear #", value = "Supprime # message(s) du chat", inline = False)
    
    embed.add_field(name = "____________________\n------> Vocal :", value="Commandes liés aux interactions vocales", inline = False)
    embed.add_field(name = "$viens", value = "Connecte le bot dans le canal vocal", inline = False)
    embed.add_field(name = "$cassetoi", value = "Déconnecte le bot du le canal vocal", inline = False)
    embed.add_field(name = "$lost", value = "Joue la meilleure musique qui existe", inline = False)

   
    await ctx.send("La liste des commandes à été envoyé par MP !")
    await author.send(embed=embed)
    
@bot.command()
async def donneznousunsigne(ctx):
    r=open("saves/signe.txt","r")
    m=r.readlines()
    l=[]
    for i in range(0,len(m)-1):
        x=m[i]
        z=len(x)
        a=x[:z-1]
        l.append(a)
    l.append(m[i+1])
    o=random.choice(l)
    await ctx.send(o)
    r.close()

@bot.command()
async def addsigne(ctx, *, signe):
    a = open("saves/signe.txt","a")
    a.write("\n" + signe)
    a.close()
    
    await ctx.send("Le signe ***" + signe + "*** a bien été ajouté !")


@bot.command(pass_context=True)
async def listesignes(ctx):
    author= ctx.message.author
    r = open("saves/signe.txt", "r")
    l_msg= discord.Embed(
        title="Listes des signes :",
        description = ' '.join(r.readlines()),
        colour = discord.Colour.purple()
        )
    
    await ctx.send("La liste des signes à été envoyé par MP !")
    await author.send(embed = l_msg)
    
    r.close()

@bot.command()
async def clear(ctx, nb_del):
    
    nb_del_un = int(nb_del) + 1
    
    await ctx.channel.purge(limit = nb_del_un)
    
    botmsg = await ctx.send("***"+ str(nb_del) +"*** messages supprimés !")
    
    time.sleep(3)
    
    await botmsg.delete()

@bot.command()
async def impardonnable(ctx):
    r=open("saves/impardonnable.txt","r")
    m=r.readlines()
    l=[]
    for i in range(0,len(m)-1):
        x=m[i]
        z=len(x)
        a=x[:z-1]
        l.append(a)
    l.append(m[i+1])
    o=random.choice(l)
    await ctx.send("\"***" + o + "***\" Empire, 2019 ")
    r.close()

@bot.command(pass_context=True)
async def lyricsimpardonnable(ctx):
    author= ctx.message.author
    r = open("saves/impardonnable.txt", "r")
    l_msg= discord.Embed(
        title="Empire - Impardonnable (2019)",
        description = ' '.join(r.readlines()),
        colour = discord.Colour.purple()
        )
    
    await ctx.send("Les lyrics ont étés envoyés par MP !")
    await author.send(embed = l_msg)
    
    r.close()

@bot.command()
async def bonbot(ctx):

    file="saves/bonbot.txt"
    with open(file,"r") as f:
        nb = f.read()
        
        new_nb = int(nb)+1
    with open(file,"w") as f:
        f.write(str(new_nb))
        
    await ctx.send("Merci, on m'a complimenté **" + str(new_nb) + "** fois !")

@bot.command()
async def timer(ctx):
    date = datetime.datetime.fromtimestamp(customTimestamp)
    await ctx.send(date.strftime("%Y-%m-%d %H:%M:%S"))

@bot.command()
async def hayato(ctx, nbhoot: int):    
    x=1
        
    while x <= nbhoot:
        await ctx.send("Hayato", tts = True)
        await ctx.send("https://media.tenor.com/images/7d38b59f80ea855671a413a692de2da3/tenor.gif")
        x=x+1

    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        source = FFmpegPCMAudio('medias/sound/hayato.mp3')
        player = voice.play(source)

@bot.command()
async def icedblue(ctx):
    await ctx.send("C'est la meilleure des bières")
    await ctx.send(file=discord.File('medias/images/iced_blue.png'))
    #await ctx.send("https://karlsberg.de/wp-content/uploads/2021/01/getraenketresor_mixery_iced_blue.png")

@bot.command()
async def dodo(ctx):    
    
    await ctx.send("Bonne nuit mon zouzou", tts = True)
    
    await ctx.send(file=discord.File('medias/images/dodo.jpg'))

    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        source = FFmpegPCMAudio('medias/sound/dodo.mp3')
        player = voice.play(source)

@bot.command()
async def hoothoot(ctx, nbhoot: int):    
    x=1
    
    await ctx.send("hoot-hoot", tts = True)
    
    while x <= nbhoot:
        await ctx.send(file=discord.File('medias/images/hoothoot.png'))
        x=x+1

    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        source = FFmpegPCMAudio('medias/sound/hoothoot.mp3')
        player = voice.play(source)

@bot.command(pass_context=True)
async def lost(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('medias/music/lost.mp3')
    player = voice.play(source)

@bot.command()
async def viens(ctx):
    channel= ctx.author.voice.channel
    await channel.connect()
    

@bot.command()
async def cassetoi(ctx):
    await ctx.voice_client.disconnect()
    
    
bot.add_cog(TestCog(bot))
bot.run(os.environ['BOT_TOKEN'])