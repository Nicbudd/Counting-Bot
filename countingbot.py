import math, discord, random, csv, datetime
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


client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


capes = 297909505621098496
austin = 396730242460418058
crapideot = 736864788927217696

countServ = 830823587417030677

def auscoin(message):
    user = message.author
    messageBits = message.content.split(" ")
    command = messageBits[1]

    time = datetime.date.today()

    nohio = discord.utils.get(client.emojis, name="nohio")

    if command == "help":
        return f"```nhi bal - Prints your balance \nnhi d20 - Roll a d20. If you roll a nat 20, you get 20 nohio.\nMore to come soon!```"

    else:

        filename = "auscoin.txt"
        try:
            file = open(filename, newline="")
        except IOError:
            return "Oops, couldn't find record file! <@!396730242460418058> fix this bitch"
        else:
            bank = list(csv.reader(file, delimiter=","))

            returnMessage = ""

            userAccount = []

            accFound = False

            for account in bank:
                if str(user.id) == account[0]:
                    userAccount = account
                    accFound = True
                    print("Account found!" + ",".join(userAccount))
                    break

            if not(accFound):
                userAccount = [str(user.id), "0", str(time)]
                bank.append(userAccount)
                print("New account opened")

             #special bits

            userAccount[0] = int(userAccount[0])
            userAccount[1] = int(userAccount[1])

            if command == "free" and user.id == 396730242460418058:
                userAccount[1] += 1
                print(userAccount[1])
                returnMessage = f"Added 1 {nohio} to your account for free! Balance: {userAccount[1]} {nohio}"

            elif command == "bal" or command == "balance":
                returnMessage = "Balance: {userAccount[1]} {nohio}"
            else:
                print(time)
                print(userAccount[2])
                if str(time) == str(userAccount[2]):
                    print("hello")
                    returnMessage = f"Sorry, you redeemed your {nohio} for today. Come back tomorrow."

                elif command == "d20" or command == "D20":
                    r = random.randint(1, 20)

                    if r == 20:
                        userAccount[1] += 20
                        truthString = f"NAT 20! Added 20 {nohio} to your account."
                    else:
                        truthString = f"{r}. No {nohio} for you."

                    returnMessage = f"Rolled a {truthString} Balance: {userAccount[1]} {nohio}"
                else:
                    returnMessage = "Command not found"


        file.close()

        file = open(filename, "w", newline="")
        bankwriter = csv.writer(file, delimiter=",")
        bankwriter.writerows(bank)
        file.close()

        print(returnMessage)
        return(returnMessage)

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
                    print("Palindrome!")
                    print(message.content)
                    print(message)
                    print("")


                if "69" in num:
                    await message.add_reaction("🍆")
                    print("🍆")
                    print(message.content)
                    print(message)
                    print("")

                if "420" in num:
                    await message.add_reaction(discord.utils.get(client.emojis, name="weedwalk"))
                    print("Blaze it")
                    print(message.content)
                    print(message)
                    print("")

                if "666" in num:
                    await message.add_reaction("😈")
                    print("😈")
                    print(message.content)
                    print(message)
                    print("")

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


        if message.content.startswith("nhi ") or message.content.startswith("nohios ") or message.content.startswith("nohio ") and message.channel.name == "nohios":
            await message.channel.send(auscoin(message))

        else:
            if "ohio" in message.content.lower() or "oh*o" in message.content.lower():
                await message.add_reaction(discord.utils.get(client.emojis, name="nohio"))



        try:
            ohioan = discord.utils.get(message.author.roles, name="Ohioan")
        except:
            ohioan = False
        else:
            ohioan = True

        if ohioan:
            if random.randint(1, 100) == 69:
                await message.channel.send("Shut up OHIOAN")





file = open("C:\TokenFolder\countingtoken.txt", "r")

for line in file:
    token = line

file.close()

client.run(token)