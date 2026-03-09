import random

rightnum = random.randint (1,10)
guessfr = 0
usinput = int(input("Input your guess here"))
guessnum = 0
guesshist = []


while guessfr == 0:
    if usinput == rightnum:
        guessfr = guessfr+1
    elif usinput > rightnum:
        print ("Too high!")
        guesshist.insert(guessnum, usinput)
        guessnum = guessnum+1
        print ("Your guess history:", guesshist)
        usinput = int(input("Input your new guess here"))
    elif usinput < rightnum:
        print ("Too low!")
        guesshist.insert(guessnum, usinput)
        guessnum = guessnum+1
        print ("Your guess history:", guesshist)
        usinput = int(input("Input your new guess here"))
    else:
        print ("Invalid input!")
        guesshist.insert(guessnum, usinput)
        guessnum = guessnum+1
        print ("Your guess history:", guesshist)
        usinput = int(input("Input your new guess here"))


print ("Number guessed!")
print ("Your guess history:", guesshist)



