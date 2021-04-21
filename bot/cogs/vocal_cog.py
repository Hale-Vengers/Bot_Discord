import discord

from dotenv import load_dotenv
from discord.ext import commands


class VocalCog(commands.Cog):
	

	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	async def viens(self, ctx):
		channel= ctx.author.voice.channel
		await channel.connect()


	@commands.command()
	async def cassetoi(self, ctx):
		await ctx.voice_client.disconnect()
