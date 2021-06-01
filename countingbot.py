import math, discord, requests


def numberinfo(message):

    channel = message.channel.name


    #find what rules the channel has

    skipinitial = ""
    allowedchar = "0123456789"
    hasnumbers = True
    integer = True


    if channel == "negative-counting":
        skipinitial = "-"

    elif channel == "counting-decimal":
        skipinitial = "0."
        integer = False

    elif channel == "binary-counting":
        allowedchar = "01"
        integer = False

    elif channel == "roman-numeral-counting":
        allowedchar = "IVXLCDM"
        integer = False

    elif channel == "hexadecimal-counting":
        allowedchar = "0123456789ABCDEF"
        integer = False

    elif channel in ["counting-but-nsfw", "counting-but-words"]:
        allowedchar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ-"
        integer = False

    elif channel in ["counting-but-gifs", "tally-counting", "unicode-counting", "counting-but-letters"]:
        hasnumbers = False
        integer = False



    #detect the number

    num = ""

    if hasnumbers:
        initial = True
        for x in message.content.upper():
            if initial == True and x in skipinitial:
                continue
            elif x in allowedchar:
                first = False
                num += x
            else:
                break


    palin = True
    for x in range(math.floor(len(num) / 2)):
        oppPair = [num[x], num[-1 * x - 1]]
        if not (oppPair[0] == oppPair[1]):
            palin = False


    if len(num) <= 2:
        palin = False

    try:
        numtest = int(num)
    except:
        integer = False


    return num, palin, integer



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


    num, palin, integer = numberinfo(message)

    if not(num == ""):

        if palin:
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

        if "fact" in message.content and integer:

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