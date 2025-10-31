# Discord BOT to show Epic Free Games

## Context
I have got a lot of things to do in my every day life and I can't go to epic games every thursdays so 
I just wanted to create a discord bot that shows the free games of thursday and I go get them if they got my interest.  
I used a debian server and turn it into a service so i can disable or enable it every time.  
To create that bot i used python and the libraries you can see under :

## Requirements 
discord.py>=2.3.2  
requests>=2.31.0  
dotenv>=1.2.1 

## Working 
This program uses a link given by epic Games that lists every game in promotions.
I parse this JSON file and find the price of 0. Then I send it to my groupchat.
