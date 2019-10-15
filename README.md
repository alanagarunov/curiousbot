# curiousbot
a discord bot made by the help of discord.py link https://github.com/Rapptz/discord.py  
this bot also requires pyOWM for one of its commands, more info on https://github.com/csparpa/pyowm  
  
This bot intends to put together a complitation of fun but relatively useful scripts and functions that can be accessed and used via discord. Here is an ever growing list of what it can do so far:  
  
1. The bot logs every message sent in every channel it is in and writes it to some file. Notice that it doesn't take into account name changes, this will likely be fixed in the future.  
2. The bot logs each reaction now as well, reactions can be used to collect statistics on funny messages. I will likely use a soon to be uploaded c++ program to cycle through the textfile created by this bot to make statistics. The bot will log the user who reacted, and the emoji that was used.  
3. As mentioned above, one of the commands includes the use of the pyOWM api in order to search and grab weather information about a particular location that you can enter, along with units and such. It then displays it in a single message.  
4. To build on accessing weather, there is also a comamnd to pull weather images from a website like https://wttr.in/ , which presents weather beautifully in ASCII characters. This is mostly taking advantage of the fact that discord will auto embbed previews of website links, which works in our favor. 



