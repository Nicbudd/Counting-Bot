import math, discord, random, csv, datetime, requests
import os


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


triesPerDay = 5

client = discord.Client()

@client.event
async def on_ready():

    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    #KEEP THIS
    if message.author == client.user:
        return

    #find the segments of the message

    segments = message.content.split(" ")

    #make some boolean variables to check what type of message it is

    """
    countServ = counting server
    directMessage = DMs
    austin = from Austin (override pretty much everything)
    """

    austin = message.author.id == 396730242460418058 #austin's ID


    if message.content == "c status" and austin:

        await message.delete()
        await message.channel.send("Hey everyone! I'm going down for a few minute while Austin configures the raspberry pi to stay running over his vacation.")


    num = ""

    for x in message.content:
        if x.isdigit():
            num += x
        elif x == "-":
            continue
        else:
            break

    if not(num == ""):

        if ispalin(num):
            await message.add_reaction(discord.utils.get(client.emojis, name="palindrome"))
            print("Palindrome!")
            print(message.content)
            print("")

        if "69" in num:
            await message.add_reaction("🍆")
            print("🍆")
            print(message.content)
            print("")

        if "420" in num:
            await message.add_reaction(discord.utils.get(client.emojis, name="weedwalk"))
            print("Blaze it")
            print(message.content)
            print("")

        if "621" in num:
            await message.add_reaction(discord.utils.get(client.emojis, name="621"))
            print("OwO")
            print(message.content)
            print("")

        if "666" in num:
            await message.add_reaction("😈")
            print("😈")
            print(message.content)
            print("")

        if "fact" in message.content:
            url = "http://www.numbersapi.com/" + num

            fact1 = requests.get(url)
            fact2 = requests.get(url + "/math")

            if fact1.status_code == 200 and fact2.status_code == 200:
                fact = fact1.text
                mathfact = fact2.text
                await message.reply(f"Fact 1: {fact}\nFact 2: {mathfact}")
            else:
                await message.reply(f"HTTP Error: {fact1.status_code} and {fact2.status_code}.")




file = open("token.config", "r")

for line in file:
    token = line

file.close()

client.run(token)