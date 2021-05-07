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


client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


capes = 297909505621098496
austin = 396730242460418058
crapideot = 736864788927217696

countServ = 830823587417030677

triesPerDay = 5

def balanceMessage(userAccount):
    nohio = discord.utils.get(client.emojis, name="nohio")
    return(f"\nBalance: {userAccount[1]} {nohio}, {triesPerDay - userAccount[3]} tries left")


def auscoin(message):

    gambaTries = 3

    user = message.author
    messageBits = message.content.split(" ")
    command = messageBits[1]

    time = datetime.date.today()

    nohio = discord.utils.get(client.emojis, name="nohio")

    if command == "help":
        return f"**Each user gets 5 tries a day.**\n`nhi bal` - Prints your balance.\n**1 Try:** \n`nhi d20` - Roll a d20. If you roll a nat 20, you get 20 {nohio}.\n`nhi d100` - Roll a d100. If you roll a nat 100, you get 100 {nohio}.\n`nhi 50/50` - Roll a 50/50 chance of getting 3 {nohio}.\n`nhi states` - Random US State, and you get 2 {nohio}. Don't get Ohio.\n**3 Tries:**\n`nhi gamble` - Do you wanna take the gamba? Big rewards, big losses."

    else:

        filename = "auscoin.txt"
        try:
            file = open(filename, newline="")
        except IOError:
            return "Oops, couldn't find record file! <@!396730242460418058> fix this bitch"
        else:
            bank = list(csv.reader(file, delimiter=","))

            userQuery = message.author.id

            """ if (command == "addBal" or command == "addbal" or command == "addTries" or command == "addtries") and user.id == austin:
                value = int(messageBits[2])
                print(messageBits[2])
                print(messageBits[3])

                try:
                    target = discord.utils.get(message.guild.users, name=messageBits[3])
                    userQuery = target.id
                except:
                    try:
                        target = discord.utils.get(message.guild.users, nick=messageBits[3])
                        userQuery = target.id
                    except:
                        return ("Could not find user")"""


            returnMessage = ""

            userAccount = []

            accFound = False

            for account in bank:
                if str(userQuery) == account[0]:
                    userAccount = account
                    accFound = True
                    break

            if not(accFound):
                userAccount = [str(userQuery), "0", str(time), "0"]
                bank.append(userAccount)

            #special bits

            userAccount[0] = int(userAccount[0])
            userAccount[1] = int(userAccount[1])
            userAccount[3] = int(userAccount[3])

            if command == "free" and user.id == austin:
                userAccount[1] += 1
                returnMessage = f"Added 1 {nohio} to your account for free! {balanceMessage(userAccount)}"

            elif command == "bal" or command == "balance":
                returnMessage = f"{balanceMessage(userAccount)}"

            else:

                if not(str(time) == str(userAccount[2])):
                    userAccount[3] = 0
                    userAccount[2] = time

                if not(userAccount[3] >= triesPerDay) or user.id == austin:
                    userAccount[3] += 1
                    returnMessage = f"Sorry, you redeemed your {nohio} for today. Come back tomorrow."

                    if command == "d20" or command == "D20" or command == "20":
                        r = random.randint(1, 20)

                        if r == 20:
                            userAccount[1] += 20
                            returnMessage = f"Rolled a NAT 20! Added 20 {nohio} to your account. {balanceMessage(userAccount)}"
                        else:
                            returnMessage = f"Rolled a {r}. No {nohio} for you. {balanceMessage(userAccount)}"

                    elif command == "d100" or command == "D100" or command == "100":
                        r = random.randint(1, 100)

                        if r == 100:
                            userAccount[1] += 100
                            returnMessage = f"Rolled a 100 wtf!! Added 100 {nohio} to your account. {balanceMessage(userAccount)}"
                        else:
                            returnMessage = f"Rolled a {r}. No {nohio} for you. {balanceMessage(userAccount)}"

                    elif command == "5050" or command == "50-50" or command == "50/50":
                        r = random.randint(1, 2)

                        if r == 1:
                            userAccount[1] += 3
                            returnMessage = f"You won the 50/50! Added 3 {nohio} to your account. {balanceMessage(userAccount)}"
                        else:
                            returnMessage = f"You lost the 50/50. No {nohio} for you. {balanceMessage(userAccount)}"

                    elif command == "gamble" or command == "gamba":
                        userAccount[3] -= 1
                        if gambaTries > triesPerDay - userAccount[3] and not(user.id == austin):
                            returnMessage = f"Not enough tries today. Gamba costs {gambaTries} tries to play. {balanceMessage(userAccount)}"
                        else:
                            userAccount[3] += 3
                            r = random.randint(1, 20)

                            if r == 1:
                                userAccount[1] *= 2
                                returnMessage = f"BIG WIN! Your balance is doubled! {balanceMessage(userAccount)}"
                            elif r == 2:
                                userAccount[1] = math.floor(userAccount[1] * 0.5)
                                returnMessage = f"big loss. Your balance is cut in half. {balanceMessage(userAccount)}"
                            elif r == 3:
                                userAccount[1] += 100
                                returnMessage = f"You gain 100 {nohio}! Yay! {balanceMessage(userAccount)}"
                            elif r == 4:
                                userAccount[1] -= 100
                                if userAccount[1] < 0:
                                    userAccount[1] = 0
                                returnMessage = f"You lose 100 {nohio}. Not Pog. {balanceMessage(userAccount)}"
                            elif r <= 6:
                                userAccount[1] += 5
                                returnMessage = f"You win 5 {nohio}. {balanceMessage(userAccount)}"
                            elif r <= 8:
                                userAccount[1] -= 1
                                if userAccount[1] < 0:
                                    userAccount[1] = 0
                                returnMessage = f"You lose 1 {nohio}. {balanceMessage(userAccount)}"
                            elif r <= 10:
                                userAccount[1] -= 2
                                if userAccount[1] < 0:
                                    userAccount[1] = 0
                                returnMessage = f"You lose 2 {nohio}. {balanceMessage(userAccount)}"
                            elif r <= 12:
                                userAccount[1] -= 5
                                if userAccount[1] < 0:
                                    userAccount[1] = 0
                                returnMessage = f"You lose 5 {nohio}. {balanceMessage(userAccount)}"
                            elif r <= 14:
                                userAccount[1] += 1
                                returnMessage = f"You win 1 {nohio}. {balanceMessage(userAccount)}"
                            elif r <= 16:
                                userAccount[1] += 2
                                returnMessage = f"You win 2 {nohio}. {balanceMessage(userAccount)}"
                            else:
                                returnMessage = f"You win nothing. {balanceMessage(userAccount)}"


                    elif command == "state" or command == "states":
                        r = random.randint(0, 49)
                        states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
                        yourState = states[r]

                        if yourState == "Ohio":
                            userAccount[1] -= 50
                            if userAccount[1] < 0:
                                userAccount[1] = 0

                            returnMessage = f"Well shit. It was Ohio. 50 points deducted from your account. {balanceMessage(userAccount)}"


                        elif yourState == "New Hampshire":
                            userAccount[1] += 5
                            returnMessage = f"You got New Hampshire! You get 5 {nohio}. {balanceMessage(userAccount)}"

                        else:
                            userAccount[1] += 2
                            returnMessage = f"You got {yourState}, you get 2 {nohio}. {balanceMessage(userAccount)}"

                    else:
                        returnMessage = "Command not found"
                        userAccount[3] -= 1

                else:
                    returnMessage = "Sorry, you've used up all your tries. Come back tomorrow."

        file.close()

        file = open(filename, "w", newline="")
        bankwriter = csv.writer(file, delimiter=",")
        bankwriter.writerows(bank)
        file.close()

        print(returnMessage)
        return returnMessage

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

        #if its a counting channel (or austin)
        if not(message.channel.name == "not-counting") or message.author.id == austin:

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

        if message.content == "counting astronauts":

            response = requests.get("http://api.open-notify.org/astros.json")
            if response.status_code == 200:
                parsed = response.json()
                personStr = ""
                for person in parsed['people']:
                    personStr += f"Astronaut: {person['name']}, Craft: {person['craft']}\n"
                await message.channel.send(personStr)
            else:
                print(response.status_code)
                await message.channel.send(f"HTTP Error: {response.status_code}")

        if message.content == "counting ?":
            response = requests.get("https://yesno.wtf/api")
            r = response.json()
            await message.channel.send(r["answer"].capitalize())
            await message.channel.send(r["image"])

        try:
            ohioan = discord.utils.get(message.author.roles, name="Ohioan")
        except:
            ohioan = False
        else:
            if ohioan == None:
                ohioan = False
            else:
                ohioan = True

        if ohioan:
            r = random.randint(1, 50)
            if r == 1:
                await message.channel.send("Shut up OHIOAN")
            elif r == 2:
                await message.channel.send("Ohioan Detected")





file = open("C:\TokenFolder\countingtoken.txt", "r")

for line in file:
    token = line

file.close()

client.run(token)