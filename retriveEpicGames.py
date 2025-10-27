#Imports
import discord
import requests
import webserver
from datetime import *
from discord.ext import tasks
import os
#Bot Initialisation
token = os.environ['discordToken']
bot = discord.Client(intents=discord.Intents.all())
CHANNEL_ID=1432199328641978368

#Date Checking (if thursday [date of Epic])
@tasks.loop(hours=24)
async def sendFreeEpicGames():
    channel=bot.get_channel(CHANNEL_ID)
    today=date.today()
    if today.weekday() == 4 :
        #Link for promotions
        epic="https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-FR&country=FR&allowCountries=FR"
        response = requests.get(epic, timeout=10)
        #Get jsonData from link
        data = response.json()
        #Check each elements 
        for i in (data['data']['Catalog']['searchStore']['elements']):
            #Check if the game is free
            if (i['price']['totalPrice']['discountPrice'] == 0):
                #Check if the title in the URL is None
                if (i['catalogNs']['mappings'] != None):
                    urlName=i['catalogNs']['mappings'][0]['pageSlug']
                    url="https://store.epicgames.com/fr/p/" + urlName
                    if channel:
                        await channel.send(
                            f"🎮{i['title']} est gratuit les gaaaaars !!!!\n\n"
                            f"🌐 Lien pour le télécharger :{url}"
                        )
                    else: 
                        print("Channel not found")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    sendFreeEpicGames.start()  # start the loop

if __name__ == '__main__':
    webserver.keep_alive()
    bot.run(token=token)

