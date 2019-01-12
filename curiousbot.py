import discord
from discord.ext.commands import Bot
from discord import Game
import random
import time
import sys #for exit commands if need

while True:
	x = time.time()

	if x >= 1546553130: #unix timestamp
		BOT_PREFIX = "€"  #your bot prefix, change it anything better than an euro symbol
		client = Bot(command_prefix=BOT_PREFIX)
		
		#the eight ball command, including data for the default help message
		@client.command(name = "8ball",
				description = "Upon using the command, you will be rewarded with an answer",
				brief = "input question, output answer")
		async def eight_ball():
			possible_responses = ["Outlook is not certain",
						"Outlook is certain",
						"Who uses microsoft outlook anyways?",
						"Definitely",
						"If deku asked this, then probably. Otherwise no.",
						"If green asked this, then no. Otherwise no.",
						"4Shrug"]
			await client.say(random.choice(possible_responses))
		
		@client.event
		async def on_message(message):
			# we do not want the bot to reply to itself
			if message.author == client.user:
				return
			pics = []
			pics = message.attachments #gets a list of data attached
			if not pics:
				msg = message.content #gets content 
				auth = message.author #gets author
				chan = message.channel #get channel (plain text, subject to change like all the rest)
				print(msg) 
				f = open("discordlog.txt", "a") #replace discordlog with the name of your file
				with open("discordlog.txt",'a',encoding = 'utf-8') as f:
					f.write(str(int(time.time())) + " ")
					f.write(str(chan) + " ")
					f.write(str(auth) + " : ") 
					f.write(msg + "\n") #notice no file close, don't know if thats an issue or not
			else:
				for p in pics: #cycle through 1 thing that was attached to message
					content = p
					auth = message.author #to see who sent the attachment
					chan = message.channel #to see where the attachment was sent
					f = open("discordlog.txt", "a")
					with open("discordlog.txt",'a',encoding = 'utf-8') as f:
						f.write(str(int(time.time())) + " ")
						f.write(str(chan) + " ")
						f.write(str(auth) + " : ")
						f.write("image ")  #so we know its an image
						f.write(str(p) + "\n")
						
			if message.content.startswith('[fuck'):
				msg = 'Hello {0.author.mention} im a something!!!'.format(message)
				await client.send_message(message.channel, msg)
			await client.process_commands(message) #makes other commands work
		
		#introducing an ALL NEW reaction logger!!!
		@client.event
		async def on_reaction_add(reaction, user):
			reacter = user.name #gets who reacted
			emoj = reaction.emoji #what the emoji actually was
			amount = reaction.count #how many times it was reacted
			r = open("reacterlog.txt","a")
			with open("reacterlog.txt",'a',encoding = 'utf-8') as r:
				r.write(reacter + " : ")
				r.write(str(emoj) + " ")
				r.write("Reacted this much: " + str(amount) + "\n")	

		@client.event
		async def on_ready():
			await client.send_message(client.get_channel("00000000000000"), "<@1111111111111111111>") #replace with channel id and user id respectively to achieve the effect described in readme
			await client.change_presence(game=Game(name='wishing wagl a happy birthd'))
			print('Logged in as')
			print(client.user.name)
			print(client.user.id)
			print('------')
			
		client.run('<replace_with_ouath>') #replace with the bots token
		
	else:
		time.sleep(5) #to save a ton of cpu
		x = time.time()
		print(int(x))
