import random

UserGuess = ""
CountryList = ["spanje", "portugal", "italie", "griekenland", "denemarken", "luxemburg", "ierland", "noorwegen", 
"oostenrijk", "verenigd koningkrijk", "polen", "tsjechie", "servie", "kroatie", "slovenie", "wit rusland"]
SecretWord = random.choice(CountryList)
CorrectGuess = 0
Lives = 8
print(SecretWord)
lengthofword = (len(SecretWord))

empyList = list()

guessedlist = list()

for letters in SecretWord:
    empyList.append("_")
print(empyList)

while Lives > 0:
    userGuess = input("Try to guess a letter: ")
    guessedlist.append(userGuess)
    print("You guessed the letter's:", guessedlist)
    indexCounter = 0
    lostLives = True
    for letter in SecretWord:
        for n in guessedlist:
            if n != userGuess:
                if letters == userGuess:
                    empyList[indexCounter] = userGuess
                    CorrectGuess = CorrectGuess + 1
                    print(" ".join(empyList))
                    lostLives = False
                indexCounter = indexCounter + 1
    if lengthofword == CorrectGuess:
        print("You win")
        print("Ënd program")
        break
    if lostLives == True:
        print("You lost a live")
        Lives = Lives - 1
        print("Amount of lives left:", Lives)

    if Lives == 0:
        print("You lose")
        print("The secret word was " , SecretWord)
        print("End program")
