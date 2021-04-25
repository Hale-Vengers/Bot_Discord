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
		emoji = '\N{THUMBS UP SIGN}'
		voice = discord.utils.get(self.bot.voice_clients, guild = ctx.guild)
  
		msg = channel.fetch_message(last_message_id)

		if voice == None:
			await ctx.send("Le bot n'est pas dans un canal vocal")
		else:
			await ctx.voice_client.disconnect()
			await msg.add_reaction(emoji)
