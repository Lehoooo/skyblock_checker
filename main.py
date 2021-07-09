# Made By Leho - github.com/Lehoooo
import requests

print("Starting Skyblock Checker - Made By github.com/Lehoooo")

loadtxt = open("usernames.txt", "r")
readtxt = loadtxt.read().split('\n')

loadresults = open("info.txt", "w")

print(f''' ________  ___  __        ___    ___ ________  ___       ________  ________  ___  __            ________  ___  ___  _______   ________  ___  __    _______   ________     
|\   ____\|\  \|\  \     |\  \  /  /|\   __  \|\  \     |\   __  \|\   ____\|\  \|\  \         |\   ____\|\  \|\  \|\  ___ \ |\   ____\|\  \|\  \ |\  ___ \ |\   __  \    
\ \  \___|\ \  \/  /|_   \ \  \/  / | \  \|\ /\ \  \    \ \  \|\  \ \  \___|\ \  \/  /|_       \ \  \___|\ \  \\\  \ \   __/|\ \  \___|\ \  \/  /|\ \   __/|\ \  \|\  \   
 \ \_____  \ \   ___  \   \ \    / / \ \   __  \ \  \    \ \  \\\  \ \  \    \ \   ___  \       \ \  \    \ \   __  \ \  \_|/_\ \  \    \ \   ___  \ \  \_|/_\ \   _  _\  
  \|____|\  \ \  \\ \  \   \/  /  /   \ \  \|\  \ \  \____\ \  \\\  \ \  \____\ \  \\ \  \       \ \  \____\ \  \ \  \ \  \_|\ \ \  \____\ \  \\ \  \ \  \_|\ \ \  \\  \| 
    ____\_\  \ \__\\ \__\__/  / /      \ \_______\ \_______\ \_______\ \_______\ \__\\ \__\       \ \_______\ \__\ \__\ \_______\ \_______\ \__\\ \__\ \_______\ \__\\ _\ 
   |\_________\|__| \|__|\___/ /        \|_______|\|_______|\|_______|\|_______|\|__| \|__|        \|_______|\|__|\|__|\|_______|\|_______|\|__| \|__|\|_______|\|__|\|__|
   \|_________|         \|___|/                                                                                                                                           
                                                                                                                                                                          
                                                                                                                                                                          ''')

for x in range(len(readtxt)):
    r = requests.get(f"https://sky.shiiyu.moe/api/v2/coins/{readtxt[x]}").json()
    if "profiles" in r:

        loadresults.write("----------\nUsername: " + str(readtxt[x]) + "\nProfiles: " + str(len(r["profiles"].keys())) + "\n")
        for a in r["profiles"].keys():
            if "bank" in r["profiles"][a]:
                print("Checked Name " + readtxt[x] + " - Profile: " + str(a) + " - Purse: " + str(round(r["profiles"][a]["purse"])) + " - Bank: " + str(round(r["profiles"][a]["bank"])))
                loadresults.write("\n  Profile: " + str(r["profiles"][a]["cute_name"]) + "\n  Purse: " + str(round(
                    r["profiles"][a]["purse"])) + "\n  Bank: " + str(round(r["profiles"][a]["bank"])) + "\n")

            else:
                print("Checked Name " + readtxt[x] + " - Profile: " + str(a) + " - Purse: " + str(round(r["profiles"][a]["purse"])) + " - Bank: 0")
                loadresults.write("\n  Profile: " + str(r["profiles"][a]["cute_name"]) + "\n  Purse: " + str(round(
                    r["profiles"][a]["purse"])) + "\n")
    else:
        print(str(readtxt[x]) + " Has No Skyblock Data - Skipping")

print("Finished! Closing TXT")
loadresults.close()
loadtxt.close()