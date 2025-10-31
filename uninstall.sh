#!/bin/bash

#Initialise variables

#Checks if there's no arguments 
if [[ $1 == "" ]]; then
	./uninstall.sh -h
	exit 0
fi

# Get arguments
while getopts "n:h" opt; do
  case $opt in
    n) name="$OPTARG" ;;
    h) echo "Uninstall your discord bot to retrieve EpicFreeGames

uninstall.sh -n name_of_the_bot
-n : the name of the bot
-h : Displays this"
exit 0;;
  esac
done

if [[ $name == "" ]];then
	echo "you have to put a name as an argument"
	exit 0
fi 
#Stopping the service
sudo systemctl disable $name.service
sudo systemctl stop $name.service

#Delete bot repertory
rm -r $(sudo find / -iname "showEpicBot" 2>/dev/null)

#Delete of the service file
sudo rm /etc/systemd/system/$name.service

#Restart services
sudo systemctl daemon-reload
clear
sudo systemctl status $name.service