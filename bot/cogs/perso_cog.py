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
	async def raph(self, ctx):
		await ctx.send("Il est tout puissant")
		
