# importing the libraries (discord.py and beautiful soup)
import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

# Prefix command used to call the bot. Modify it if you want to use another prefix command
# Example : "/alma", ".alma", "!alma", and so on... (the "alma" call text can be modified too, see below)
client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    # Text shown in the terminal just to know if the bot is running fine.
    print("The bot is ready")

@client.command()
async def alma(ctx):
    url="http://www.krosmoz.com/fr/almanax"

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")

    # Finding the "fleft" class in the "p" tag (Almanax's daily offering)
    offrande = soup.find("p", attrs={"class": "fleft"})

    # Finding the "more" class in the "div" tag (Almanax's daily bonus)
    bonus = soup.find("div", attrs={"class": "more"})

    # The bot will then write the Almanax daily offering and bonus in the Discord chat you typed the command in
    await ctx.send("```Almanax : {}``````Bonus : {}```".format(offrande.text.strip().partition(".")[0], bonus.text.strip().partition(".")[0]))

# You will need to have a bot and it's token, and just simply put it in the quotes
#client.run('Enter your bot token here')
