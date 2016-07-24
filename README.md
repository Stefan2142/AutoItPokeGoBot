# AutoItPokeGoBot
Automation script for GO-Bot by AnthonyOSX

While that bot works great I found out that if you are farming one area..you will end up with bunch of same pokemons. In order to make pokedex more diversable you have to manually change coordinates to change area every couple of hours (or minutes). 
It is based on GO Bot v0.0.4 [BETA]

# Requirements:
Python 2.7
PyWin32 - https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/pywin32-220.win32-py2.7.exe/download
GO Bot v0.0.4 [BETA]

# Usage:
Open the script and change the path to your 'GO Bot.exe' (shell.Run() command) file so script can run. You can leave it over night or afternoon and it will automatically go through given coordinates. Coordinates are given in a list of two-sized tuple in a variable called 'coordinates'. Variable 'duration' - how much will bot farm given location. Variable 'rest' - how much whill script wait until it bot proceeds so you don't get softbanned.

# Important:
win32api.Sleep() uses miliseconds and time.sleep() uses seconds;

Don't interact with other windows or programs while running the script..just leave it like that;

If this gets welcomed by the community I could change it to run with both v0.0.4 and v0.0.5. Make it run with console arguments, run in background. Other suggestions are welcomed too
