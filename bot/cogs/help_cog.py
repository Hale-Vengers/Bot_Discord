import discord

from dotenv import load_dotenv
from discord.ext import commands


class HelpCog(commands.Cog):
	

	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	async def help(self, ctx):
		await ctx.send("La commande d'aide est $aide :)")


	@commands.command(pass_context=True)
	async def aide(self, ctx):
		author= ctx.message.author
	
		embed = discord.Embed(
			colour = discord.Colour.purple(),
			title = "--- Page d'aide ---"
			)
	
		embed.set_thumbnail(url = "https://media.discordapp.net/attachments/813145774320910359/824010122581114970/received_187979142621558.jpeg?width=300&height=300")
	
		embed.add_field(name = "____________________\n------> Bonus :", value="Commandes bonus", inline = False)
		embed.add_field(name = "$aide", value = "Envoi la page que vous voyez actuellement", inline = False)
		embed.add_field(name = "$bonbot", value = "Remercie le bot pour ses loyaux services", inline = False)
		embed.add_field(name = "$dodo", value = "Souhaite une bonne nuit", inline = False)
		embed.add_field(name = "$hayato #", value = "Invoque Hayato # fois", inline = False)
		embed.add_field(name = "$icedblue", value = "Réponds à la question \"quelle est la meilleure des bières ?\"", inline = False)
	
		embed.add_field(name = "____________________\n------> Empire :", value="Commandes dédiés au rappeur EMPIRE", inline = False)
		embed.add_field(name = "$impardonnable", value = "Sors une quote de son son Impardonnable", inline = False)
		embed.add_field(name = "$lyricsimpardonnable", value = "Envoi en MP les lyrics d'Impardonnable.", inline = False)
	
		embed.add_field(name = "____________________\n------> Personnalisés :", value="Commandes dédiés aux Hale-Vengers", inline = False)
		embed.add_field(name = "$creerprofil", value = "Crée un profil", inline = False)
		embed.add_field(name = "$listeprofils", value = "Montre la liste de tout les profils existants", inline = False)
		embed.add_field(name = "$surnom #####", value = "Cette commande permet de se définir un surnom (ici #####)", inline = False)
		embed.add_field(name = "$voirprofil", value = "Consulte le surnom et le niveau du profil", inline = False)

		embed.add_field(name = "____________________\n------> Profil :", value="Commandes dédiés aux profils", inline = False)
		embed.add_field(name = "$fantomas", value = "Deviens FANTOMAS", inline = False)
		embed.add_field(name = "$hale", value = "Juste Hale.", inline = False)
		embed.add_field(name = "$raph", value = "?", inline = False)

		embed.add_field(name = "____________________\n------> Signes :", value="Commandes liés au système de signes", inline = False)
		embed.add_field(name = "$addsigne ######", value = "Cette commande permet d'ajouter une phrase (ici ######) dans la liste de signes.", inline = False)
		embed.add_field(name = "$listesignes", value = "Cette commande permet de lister les différentes phrases", inline = False)
		embed.add_field(name = "$donneznousunsigne", value = "Cette commande donne un signe au hasard parmi la liste.", inline = False)
	
		embed.add_field(name = "____________________\n------> Textuels :", value="Commandes dédiés au chat", inline = False)
		embed.add_field(name = "$clear #", value = "Supprime # message(s) du chat", inline = False)
	
		embed.add_field(name = "____________________\n------> Vocal :", value="Commandes liés aux interactions vocales", inline = False)
		embed.add_field(name = "$viens", value = "Connecte le bot dans le canal vocal", inline = False)
		embed.add_field(name = "$cassetoi", value = "Déconnecte le bot du le canal vocal", inline = False)
		embed.add_field(name = "$lost", value = "Joue la meilleure musique qui existe", inline = False)
	
	
		await ctx.send("La liste des commandes à été envoyé par MP !")
		await author.send(embed=embed)