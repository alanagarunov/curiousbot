import discord
from discord.ext.commands import Bot
from discord import Game
import random
import time
import sys #for exit commands if need

while True:
	x = time.time()

	if x >= 1546553130: #unix timestamp
		BOT_PREFIX = "€"
		client = Bot(command_prefix=BOT_PREFIX)
		
		@client.event
		async def on_message(message):
			# we do not want the bot to reply to itself
			if message.author == client.user:
				return
			print(message) #prints the message to console
			msg = message.content #gets content 
			auth = message.author #gets author
			print(msg) 
			f = open("discordlog.txt", "a") #replace discordlog with the name of your file
			with open("discordlog.txt",'a',encoding = 'utf-8') as f:
				f.write(str(int(time.time())) + " ")
				f.write(str(auth) + " : ") 
				f.write(msg + "\n") #notice no file close, don't know if thats an issue or not
				
			if message.content.startswith('[fuck'):
				msg = 'Hello {0.author.mention} im a something!!!'.format(message)
				await client.send_message(message.channel, msg)
		

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
