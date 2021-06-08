
# Curiousbot

This is a Discord bot , made using the discord.py api found here: https://github.com/Rapptz/discord.py

This bot also utilizes a second api, pyOWM, for weather found here: https://github.com/csparpa/pyowm

There are many uses of the bot described in the features section. Any feature that has complex interactive ability will described in more detail in the Usage section.

## Setup
To setup all requirements and your virtual environments just follow the following string of text. Execute each line one by one. (Note: Windows specific instructions, Linux differs slightly)
```
python -m venv env
source env/scripts/activate
pip install -r requirements.txt
```
To exit your virtual environment, execute
```
deactivate
```

To run the bot, make sure you have entered your bot's token, then execute the following
```
python curiousbot.py
```
You should see a message that says "We have logged in as \<username\>#\<discriminator\>" after a few seconds.

## Usage/Examples for Stock Simulator
Note: people wishing to create a profile should attempt to buy one stock (might need to do it twice).

In order to trade a stock, use the following command:
```
<prefix> $<ticker> <buy, sell> <amount>
```
Where prefix is your bot's prefix, and ticker is the ticker symbol of your stock. The amount refers to the amount of shares.


If you would like to view your profile, use the following command:
```
<prefix> getprofilevalue
```
Where prefix is your bot's prefix, and it will display how much (paper) money you currently have.

If you are just interested in the current stock price, you can use:
```
<prefix> getstockvalue
```
Where prefix is your bot's prefix, and it will display the stock's current price.


Markov chain commands:
To be explained.



  
## Features

- Logging Capabilities: Logs all messages where the bot has read messages permissions and stores it locally.
- Stock Simulator: Buy and sell a (virtual) stock in chat.
- Markov Chain Text Generator (Python Version)
- Weather Checking from chat. Uses both api access and discord embedding via the website https://wttr.in 




