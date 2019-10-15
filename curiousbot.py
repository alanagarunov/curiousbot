#Required imports
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import random
import sys

#Function imports
from owofy import owofunction
from checkweather import thechecker
from sexyweather import simpleweather
 
#client = discord.client()
client = Bot(command_prefix='&')
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
#used to log messages where bot has view messages role
@client.event
async def on_message(message):
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
            f.write(msg + "\n") #notice no file close, unneeded, handeld automatically
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

 
    if message.content.startswith('WELOME'):
        await message.channel.send('WELOME')
    #the bot will not recognize commands without this line
    await client.process_commands(message)
 
#logs who reacts and what they reacted with on messages
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

#text modifier command
@client.command(name="owofy")
async def owo_translater(ctx, cutemessage):
    try:
        text0 = []
        text0 = owofunction(cutemessage)
    except BadArgumentError:
            await ctx.send("hi, youw input contains a quotation which wiww make python vewwy angwy! pwease dont do ok")
    await ctx.send("(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ " + "".join(text0) + " (´･ω･`)")

#looks the weather up, provides a lot of info, uses pyOWM api
@client.command(name = "checkweather",
                description = "yeah, it checks the weather btw",
                brief = "input location, output atmospheric conditions. Usage: City,Country")
async def lookupweather(ctx, request, unit, loc):
    theinfo = []
    theinfo = thechecker(request, unit, loc)
    if request == 'search':
        await ctx.send("Your local maximum temperature: " + theinfo[0] + theinfo[4] + "\n" +
                        "Your local minimum temperature: " + theinfo[1] + theinfo[4] + "\n" +
                        "Your actual temperature: " + theinfo[2] + theinfo[4] + "\n" +
                        "And your barometric pressure: " + theinfo[3] + " mb" + "\n" +
                        "Conditions: " + theinfo[5])

#takes avadvantage of discord automatically embbedding websites, works on the same principle of checkweather but pastes a url of
#a known weather site with information in a picture
@client.command(name = "sexyweather",
                description = "displays weather in an easier way",
                brief = "much better than the weather api thing")
async def sexyweather(ctx, request, loc):
    someurl = simpleweather(request, loc)
    await ctx.send(someurl)
 
client.run('<token>')
