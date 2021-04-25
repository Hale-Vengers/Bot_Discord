import datetime
import discord
import sqlite3
import time
import os

from dotenv import load_dotenv
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get

from cogs.bdd_cog import BddCog
from cogs.empire_cog import EmpireCog
from cogs.help_cog import HelpCog
from cogs.perso_cog import PersoCog
from cogs.signes_cog import SignesCog
from cogs.vocal_cog import VocalCog
from cogs.youtube_cog import YoutubeCog

load_dotenv()

bot = commands.Bot(command_prefix='$', help_command=None)

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

		channel = ctx.message.author.voice.channel
		voice = get(bot.voice_clients, guild=ctx.guild)
		if voice and voice.is_connected():
			await voice.move_to(channel)
		else:
			voice = await channel.connect()
			source = FFmpegPCMAudio('medias/sound/hoothoot.mp3')
			player = voice.play(source)
		
	await bot.process_commands(message)
 

@bot.command()
async def clear(ctx, nb_del):
	
	nb_del_un = int(nb_del) + 1
	
	await ctx.channel.purge(limit = nb_del_un)
	
	botmsg = await ctx.send("***"+ str(nb_del) +"*** messages supprimés !")
	
	time.sleep(3)
	
	await botmsg.delete()

@bot.command()
async def bonbot(ctx):

	authorname = str(ctx.message.author)
	authorid = str(ctx.message.author.id)

	conn = sqlite3.connect('saves/save.db') 
 
	c = conn.cursor()
	c.execute("SELECT nb_bonbot FROM BONBOT B, USERS U WHERE U.id = B.id AND U.discord_id = ?", [authorid])

	nb_bonbot = int(str(c.fetchone())[1:-2])

	nb_bonbot = nb_bonbot + 1

	t = (nb_bonbot, authorid)

	c.execute("UPDATE BONBOT SET nb_bonbot=? where id=(SELECT id FROM USERS where discord_id=?)", t)

	await ctx.send("Merci **" + authorname + "**, tu m'a complimenté déjà **" + str(nb_bonbot) + "** fois !")

	conn.commit()
	c.close()
	conn.close()

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

@bot.command(pass_context=True)
async def lost(ctx):
	
	authorname = str(ctx.message.author)
	authorid = str(ctx.message.author.id)

	channel = ctx.message.author.voice.channel
	voice = get(bot.voice_clients, guild=ctx.guild)
	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()
	source = FFmpegPCMAudio('medias/music/lost.mp3')
	player = voice.play(source)

	conn = sqlite3.connect('saves/save.db') 
 
	c = conn.cursor()
	c.execute("SELECT nb_lost FROM LOST L, USERS U WHERE U.id = L.id AND U.discord_id = ?", [authorid])

	nb_lost = int(str(c.fetchone())[1:-2])

	nb_lost = nb_lost + 1

	t = (nb_lost, authorid)

	c.execute("UPDATE LOST SET nb_lost=? where id=(SELECT id FROM USERS where discord_id=?)", t)

	await ctx.send("**" + authorname + "** à joué Lost **" + str(nb_lost) + "** fois")

	conn.commit()
	c.close()
	conn.close()


bot.add_cog(BddCog(bot))
bot.add_cog(EmpireCog(bot))
bot.add_cog(HelpCog(bot))
bot.add_cog(PersoCog(bot))
bot.add_cog(SignesCog(bot))
bot.add_cog(VocalCog(bot))
bot.add_cog(YoutubeCog(bot))

bot.run(os.environ['BOT_TOKEN'])