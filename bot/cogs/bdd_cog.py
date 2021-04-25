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

		conn = sqlite3.connect('saves/save.db')

		authorname = str(ctx.message.author)
		authorid = str(ctx.message.author.id)

		t = (authorname, authorname, authorid)

		c = conn.cursor()
		
		c.execute("INSERT OR IGNORE INTO USERS (id, name, nickname, discord_id) VALUES (NULL, ?, ?, ?);", t)
		c.execute("INSERT OR IGNORE INTO LEVEL (id, lvl, exp) VALUES (last_insert_rowid(), 1, 0);")
		c.execute("INSERT OR IGNORE INTO LOST (id, nb_lost) VALUES (last_insert_rowid(), 0);")
		c.execute("INSERT OR IGNORE INTO BONBOT (id, nb_bonbot) VALUES (last_insert_rowid(), 0)")

		conn.commit()
		c.close()
		conn.close()
  		
		await ctx.send("Un profil pour **" + authorname + "** à bien été crée !")


	@commands.command(pass_context=True)
	async def voirprofil(self, ctx):

		conn = sqlite3.connect('saves/save.db')

		authorid = str(ctx.message.author.id)

		c = conn.cursor()
		
		c.execute("SELECT name, nickname, L.lvl, R.rankname, L.exp FROM USERS U, LEVEL L, RANK R WHERE U.id = L.id AND L.lvl = R.lvl AND discord_id = ?", [authorid])
		await ctx.send(c.fetchone())

		conn.commit()
		c.close()
		conn.close()


	@commands.command(pass_context=True)
	async def listeprofils(self, ctx):

		conn = sqlite3.connect('saves/save.db')

		c = conn.cursor()
		
		c.execute("SELECT name, nickname, L.lvl, R.rankname, L.exp FROM USERS U, LEVEL L, RANK R WHERE U.id = L.id AND L.lvl = R.lvl")
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


	@commands.command(pass_context=True)
	async def surnom(self, ctx, *, nickname):

		conn = sqlite3.connect('saves/save.db')
  		
		author= ctx.message.author
		authorname = str(ctx.message.author)
		authorid = str(ctx.message.author.id)

		t = (nickname, authorid)
  
		c = conn.cursor()
		
		c.execute("UPDATE USERS SET nickname=? WHERE discord_id=?", t)
  
		await author.edit(nick=nickname)

		await ctx.send("Le surnom de **" + authorname + "** est désormais *" + nickname + "*")

		conn.commit()
		c.close()
		conn.close()