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

		@client.command()
		async def eight_ball(name='8ball',
							 description='eventually this will be replaced by something smarter or better',
							 brief='ask a question and it will answer, smartly',
							 aliases=['eightball']):
			possible_responses = [
				'no',
				'yes',
				'maybe',
				'4Shrug',]
			await client.say(random.choice(possible_responses))
			
		
		@client.event
		async def on_message(message):
			# we do not want the bot to reply to itself
			if message.author == client.user:
				return
				
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
