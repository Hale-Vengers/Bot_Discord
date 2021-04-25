import discord

from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
import urllib.parse, urllib.request, re


class YoutubeCog(commands.Cog):
	

	def __init__(self, bot, *, volume=0.5):
		self.bot = bot

	""" @commands.command()
	async def ytb(self, ctx, *, url):

		voiceChannel= discord.utils.get(ctx.guild.voice_channels, name="test")
		voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
		if not voice.is_connected():
			await voiceChannel.connect()
		
	@commands.command()
	async def yt(self, ctx, *, search):

		query_string = urllib.parse.urlencode({"search_query": search})
		htm_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
		search_results = re.findall(r"/watch\?v=(.{11})", htm_content.read().decode())
		link = "http://www.youtube.com/watch?v=" + search_results[0]
		await ctx.send(link) """