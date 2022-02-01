# Required imports
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import socket
import random
import sys
from gpiozero import CPUTemperature
from timeloop import Timeloop

# Function imports
from owofy import owofunction
from checkweather import thechecker
from sexyweather import simpleweather
from stockssimulator import adddata
from stockssimulator import getdata
from stockssimulator import getstockprice
from markovread import mainadder
from markovgenerate import maingenerator

# client = discord.client()
client = Bot(command_prefix="<prefix> ")


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):

    msgtemp = message.content

    # tempchannel = message.channel
    # print(tempchannel)
    # if tempchannel == "<name_of_channel>":

    if not message.author.bot:
        msgforchains = message.content
        mainadder(msgforchains, "<name_of_channel>")

    personname = message.author.id
    if str(personname) == "<user_id>":
        msgforchains = message.content
        mainadder(msgforchains, "<same_as_filename>")
    elif str(personname) == "<user_id>":
        msgforchains = message.content
        mainadder(msgforchains, "<same_as_filename>")
    elif str(personname) == "<user_id>" and (
        str(message.channel) != ("<name_of_channel>" or "<name_of_channel>")
    ):
        msgforchains = message.content
        mainadder(msgforchains, "<same_as_filename>")
    elif str(personname) == "<user_id>":
        msgforchains = message.content
        mainadder(msgforchains, "<same_as_filename>")
    elif str(personname) == "<user_id>" and (
        str(message.channel) != ("<name_of_channel>" or "<name_of_channel>")
    ):
        msgforchains = message.content
        mainadder(msgforchains, "<same_as_filename>")

    pics = []
    pics = message.attachments  # gets a list of data attached
    if not pics:
        msg = message.content  # gets content
        auth = message.author  # gets author
        chan = (
            message.channel
        )  # get channel (plain text, subject to change like all the rest)
        print(msg)
        f = open("discordlog.txt", "a")  # replace discordlog with the name of your file
        with open("discordlog.txt", "a", encoding="utf-8") as f:
            f.write(str(int(time.time())) + " ")
            f.write(str(chan) + " ")
            f.write(str(auth) + " : ")
            f.write(
                msg + "\n"
            )  # notice no file close, don't know if thats an issue or not
    else:
        for p in pics:  # cycle through 1 thing that was attached to message
            content = p
            auth = message.author  # to see who sent the attachment
            chan = message.channel  # to see where the attachment was sent
            f = open("discordlog.txt", "a")
            with open("discordlog.txt", "a", encoding="utf-8") as f:
                f.write(str(int(time.time())) + " ")
                f.write(str(chan) + " ")
                f.write(str(auth) + " : ")
                f.write("image ")  # so we know its an image
                f.write(str(p) + "\n")
    # elif message.author.id == "<user_id>"
    #   text = message.content
    #   print(text)

    if message.content.startswith("WELOME") and not message.author.bot:
        await message.channel.send("WELOME")
    elif message.content.startswith("welome") and not message.author.bot:
        await message.channel.send("WELOME")

    await client.process_commands(message)


@client.event
async def on_reaction_add(reaction, user):
    reacter = user.name  # gets who reacted
    emoj = reaction.emoji  # what the emoji actually was
    amount = reaction.count  # how many times it was reacted
    r = open("reacterlog.txt", "a")
    with open("reacterlog.txt", "a", encoding="utf-8") as r:
        r.write(reacter + " : ")
        r.write(str(emoj) + " ")
        r.write("Reacted this much: " + str(amount) + "\n")


# this was really just made when i was first learning how to use this api
@client.command(name="owofy", brief="Makes your text cute.")
async def owo_translater(ctx, cutemessage):
    try:
        text0 = []
        text0 = owofunction(cutemessage)
    except BadArgumentError:
        await ctx.send(
            "hi, youw input contains a quotation which wiww make python vewwy angwy! pwease dont do that ok"
        )
    await ctx.send("(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ " + "".join(text0) + " (´･ω･`)")


@client.command(
    name="checkweather",
    description="yeah, it checks the weather btw",
    brief="input location, output atmospheric conditions. Usage: City,Country",
)
async def lookupweather(ctx, request, unit, loc):
    theinfo = []
    theinfo = thechecker(request, unit, loc)
    if request == "search":
        await ctx.send(
            "Your local maximum temperature: "
            + theinfo[0]
            + theinfo[4]
            + "\n"
            + "Your local minimum temperature: "
            + theinfo[1]
            + theinfo[4]
            + "\n"
            + "Your actual temperature: "
            + theinfo[2]
            + theinfo[4]
            + "\n"
            + "And your barometric pressure: "
            + theinfo[3]
            + " mb"
            + "\n"
            + "Conditions: "
            + theinfo[5]
        )


# comment out command if on Windows
@client.command(
    name="checksystem",
    description="Checks the status of the sytem",
    brief="Checks the status of the sytem",
)
async def pisystem(ctx):
    cpu = CPUTemperature()
    ctx.send("The CPU temperature is: " + str(cpu.temperature))


@client.command(
    name="ping",
    description="Is that website working??? is discord down??? Try and find out",
    brief="use <prefix> ping discord_<region>",
)
async def pingcommand(ctx, REMOTE_SERVER):
    try:
        south = "us-south373.discord.gg"
        west = "us-west937.discord.gg"
        central = "us-central307.discord.gg"
        eu = "eu-central971.discord.gg"
        africa = "southafrica996.discord.gg"
        japan = "japan906.discord.gg"
        aus = "sydney334.discord.gg"
        # listofregions = [south,west,central,eu,africa,japan,aus]
        if REMOTE_SERVER == "discord_south":
            REMOTE_SERVER = south
        elif REMOTE_SERVER == "discord_west":
            REMOTE_SERVER = west
        elif REMOTE_SERVER == "discord_central":
            REMOTE_SERVER = central
        elif REMOTE_SERVER == "discord_eu":
            REMOTE_SERVER = eu
        elif REMOTE_SERVER == "discord_africa":
            REMOTE_SERVER = africa
        elif REMOTE_SERVER == "discord_japan":
            REMOTE_SERVER = japan
        elif REMOTE_SERVER == "discord_aus":
            REMOTE_SERVER = aus
        host = socket.gethostbyname(REMOTE_SERVER)
        before = time.perf_counter()
        s = socket.create_connection((host, 80), 2)
        after = time.perf_counter()
        elapsedtime = (after - before) * 1000
        await ctx.send("Ping time was " + str(elapsedtime) + " ms")
    except Exception as e:
        elapsedtime = "Ping returned error. Error in question: "
        await ctx.send(elapsedtime + str(e))


@client.command(
    name="sexyweather",
    description="displays weather in an easier way",
    brief="USAGE: sexyweather <sexy, simple> <your location in one word>",
)
async def sexyweather(ctx, request, loc):
    try:
        someurl = simpleweather(request, loc)
        await ctx.send(someurl)
    except Exception as e:
        await ctx.send(
            "Error has occured, Ping @curiousdoge#4240 with the following error message: "
            + str(e)
        )
        
@client.command(name = "wordle",
                description = "More descriptive text here",
                breif = "descriptive text")
async def wordle(ctx, arg):
    word = "sushi"
    word_freq = {}
  
    for i in word:
        if i in word_freq:
            word_freq[i] += 1
        else:
            word_freq[i] = 1

    answer = list(word)
    user_word = list(arg)

    result = ""

    if len(user_word) == 5:
        for x, y in zip(answer, user_word):
            if x == y:
                result += '\U0001F7E9'
                word_freq[y] -= 1
            else:
                result += '\u2B1B' 

        for x, y, r in zip(answer, user_word, range(0,5)):
            if y in word and word_freq[y] > 0:
                result = result[:r] + '\U0001F7E8' + result[r+1:]
                word_freq[y] -= 1
        await ctx.send(result)
    else:
        await ctx.send("Word is too long or short, must be 5 characters.")


@client.command(
    name="$<Ticker_name>",
    description="filler",
    brief="trade stocks. USAGE: $<Ticker_name> <buy, sell> <amount>",
)
async def stockssimulator(ctx, stocktype, shareamount):
    trader = ctx.author
    finalmessage = adddata(trader, stocktype, shareamount)
    await ctx.send(finalmessage)


@client.command(
    name="getportfoliovalue", description="filler", brief="shows your portfolio valie"
)
async def stockssimulatorvalue(ctx):
    trader = ctx.author
    finalmessage = getdata(trader)
    await ctx.send(finalmessage)


@client.command(
    name="getstockvalue", description="filler", brief="shows current stock value"
)
async def stockssimulatorstockvalue(ctx):
    # trader = ctx.author
    finalmessage = getstockprice()
    await ctx.send(finalmessage)


client.run("<Token>")
