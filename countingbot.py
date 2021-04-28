import math
import discord
import os
import random

def ispalin(num):
    num = str(abs(int(num)))

    palin = True
    for x in range(math.floor(len(num) / 2)):
        oppPair = [num[x], num[-1 * x - 1]]
        if not (oppPair[0] == oppPair[1]):
            palin = False

    if int(num) < 100:
        palin = False

    return palin


client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


capes = 297909505621098496
austin = 396730242460418058
crapideot = 736864788927217696

countServ = 830823587417030677

@client.event
async def on_message(message):
    #KEEP THIS
    if message.author == client.user:
        return



    #check to make sure we don't post cringe to counting server
    try:
        guildId = message.guild.id
    except:
        testCountServ = False
    else:
        if guildId == countServ:
            testCountServ = True
        else:
            testCountServ = False

    #if counting server
    if testCountServ:

        #if its a counting channel
        if not(message.channel.name == "not-counting"):

            num = ""

            for x in message.content:
                if x.isdigit():
                    num += x

            if not(num == ""):

                if ispalin(num):
                    await message.add_reaction(discord.utils.get(client.emojis, name="palindrome"))

                if "69" in num:
                    await message.add_reaction("🍆")
                    print("🍆")
                    print(message)

                if "420" in num:
                    await message.add_reaction(discord.utils.get(client.emojis, name="weedwalk"))
                    print("Blaze it")
                    print(message)

                if "666" in num:
                    await message.add_reaction("😈")
                    print("😈")
                    print(message)

    else:

        #post cringe
        if "hi" in message.content.lower() and "counting" in message.content.lower():
            author = message.author.id
            if author == capes:
                await message.channel.send("Merp")
            elif author == crapideot:
                await message.channel.send("Hi Crap!")
            elif author == austin:
                await message.channel.send("Hi Austin!")
            else:
                await message.channel.send(f"Hi {message.author.name}")

        if "ohio" in message.content.lower() or "oh*o" in message.content.lower():

            await message.add_reaction(discord.utils.get(client.emojis, name="nohio"))

        if not(discord.utils.get(message.author.roles, name="Ohioan") == None):
            if random.randint(1, 100) == 69:
                await message.channel.send("Shut up OHIOAN")


file = open("C:\TokenFolder\countingtoken.txt", "r")

for line in file:
    token = line

file.close()

client.run(token)