# curiousbot
a discord bot made by the help of discord.py link https://github.com/Rapptz/discord.py

This bot is very simple, a simple descripition of all the bot does:
1. Upon the bots join, it will send a message to a specific channel in a server its in (you'll have to supply the channel id yourself) I have it to ping someone.
2. The bot logs every message sent in every channel it is in and writes it to some file. Notice that it doesn't take into account name changes, this will likely be fixed in the future.
3. The bot logs each reaction now as well, reactions can be used to collect statistics on funny messages. I will likely use a soon to be uploaded c++ program to cycle through the textfile created by this bot to make statistics. The bot will log the user who reacted, and the emoji that was used.
4. The eight_ball command is working again hooray!!! Use the command while asking it a question and it'll spit a random answer.
5. A simple send message function that will send a message when someone invokes it with the bot_prefix and keyword. Notice in this version that i made a different bot_prefix hardwired in the command, this is because the bot in incredibly scuffed.
6. The entire thing is wrapped around a time loop so that it executes at a specific time. 


