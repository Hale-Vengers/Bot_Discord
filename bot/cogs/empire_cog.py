import discord
import random

from dotenv import load_dotenv
from discord.ext import commands


class EmpireCog(commands.Cog):
	

	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	async def impardonnable(self, ctx):
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

	@commands.command(pass_context=True)
	async def lyricsimpardonnable(self, ctx):
		author= ctx.message.author
		r = open("saves/impardonnable.txt", "r")
		l_msg= discord.Embed(
			title="Empire - Impardonnable (2019)",
			description = ' '.join(r.readlines()),
			colour = discord.Colour.purple()
		)
		
		l_msg.set_thumbnail(url = "https://cdn.discordapp.com/attachments/833406887847657522/834190329426346044/AAUvwnh7d0eEUkjHJPiCpkVXSWJKo_s79NDLxswgeiKes88-c-k-c0x00ffffff-no-rj.png")
		await ctx.send("Les lyrics ont étés envoyés par MP !")
		
		await author.send(embed = l_msg)
	
		r.close()