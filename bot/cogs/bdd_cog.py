import discord
import sqlite3
import re

from dotenv import load_dotenv
from discord.ext import commands

class BddCog(commands.Cog):
	

	def __init__(self, bot):
		self.bot = bot


	@commands.command(pass_context=True)
	async def creerprofil(self, ctx):

		conn = sqlite3.connect('saves/save2.db')

		authorname = str(ctx.message.author)
		authorid = str(ctx.message.author.id)

		t = (authorname, authorid)

		c = conn.cursor()
		
		c.execute("INSERT OR IGNORE INTO USERS (name, discord_id) VALUES (?, ?)", t)

		conn.commit()
		c.close()
		conn.close()
  		
		await ctx.send("Un compte pour **" + authorname + "** à bien été crée !")


	@commands.command(pass_context=True)
	async def voirprofil(self, ctx):

		conn = sqlite3.connect('saves/save2.db')

		authorid = str(ctx.message.author.id)

		c = conn.cursor()
		
		c.execute("SELECT * FROM USERS WHERE discord_id = ?", [authorid])
		await ctx.send(c.fetchone())

		conn.commit()
		c.close()
		conn.close()


	@commands.command(pass_context=True)
	async def listeprofils(self, ctx):

		conn = sqlite3.connect('saves/save2.db')

		c = conn.cursor()
		
		c.execute("SELECT * FROM USERS")
		data = str(c.fetchall()).replace("), ", ")\n")[1:-1]

		l_msg= discord.Embed(
			title="Listes des profils",
			description = data,
			colour = discord.Colour.purple()
		)
		
		await ctx.send(embed = l_msg)

		conn.commit()
		c.close()
		conn.close()

