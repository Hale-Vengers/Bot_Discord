import discord

from dotenv import load_dotenv
from discord.ext import commands


class PersoCog(commands.Cog):
	

	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	async def fantomas(self, ctx):
		author= ctx.message.author
	
		await author.edit(nick="FANTOMAS")
		await ctx.send("Maintenan tu é 1 FANTOMAS")
	
 
	@commands.command()
	async def hale(self, ctx):
		await ctx.send("Bien et bon")


	@commands.command()
	async def hoothoot(self, ctx, nbhoot: int):    
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
	
 
	@commands.command()
	async def raph(self, ctx):
		await ctx.send("Il est tout puissant")
		
