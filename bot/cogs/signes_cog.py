import discord
import random

from dotenv import load_dotenv
from discord.ext import commands


class SignesCog(commands.Cog):
	
 
	def __init__(self, bot):
		self.bot = bot

	  
	@commands.command()
	async def donneznousunsigne(self, ctx):
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
	
	
	@commands.command()
	async def addsigne(self, ctx, *, signe):
		a = open("saves/signe.txt","a")
		a.write("\n" + signe)
		a.close()
		
		await ctx.send("Le signe ***" + signe + "*** a bien été ajouté !")
	
	
	@commands.command(pass_context=True)
	async def listesignes(self, ctx):
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