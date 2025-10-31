# Installation
- Take the file from github
- Create a .env file with CHANNEL_ID & your bot token
Now you can run it BUT if u want it to function without using "&" or one of your terminal you have to turn it into a service :

## Service
```bash
sudo nano /etc/systemd/system/<nameOfYourBot> :

[Unit]
Description=Retrieve Epic Games Discord Bot Service 
After=network.target # Launchs after 

[Service]
Type=simple
User=yourUser
WorkingDirectory=/your/path/to/bot/directory
ExecStart=/usr/bin/python3 /your/path/to/bot.py
Restart=on-failure		#Restart if service Crashes
RestartSec=5			    #Take 5s to restart

[Install]
WantedBy=multi-user.target
```
Restart all the services : ```sudo systemctl daemon-reload```  
Enable the bot (so it starts at boot) : ```sudo systemctl enable <nameOfYourBot>```  
Start your service : ```sudo systemctl daemon-reload <nameOfYourBot>```  
  
PS : Be sure that you've given the right permissions to the bot because i really got problems with it
