#Kade Donohoue
#5/19/23
#Treasure hunting adventure game

import random

def main():
    treasures = [["silver", "gold", "gem"], ["decorated rock", "mask", "sword"], ["map", "money", "mysterious device"]]
    collectedTreasures = []
    numberOfTries = 0

    while True:
        attempt = input("Do you want to try collecting a treasure? yes or no.")

        if (attempt == "yes"):

            numberOfTries = numberOfTries+1

            #try to collect a random treasure 1/3 chance with 3 tries
            for chest in treasures:
                if (random.randrange(1,4) == 2):
                    collectedTreasures.append(chest[random.randrange(0,len(chest))])
                    print("You collected: " + str(collectedTreasures[len(collectedTreasures)-1]))

        else:
            break
        if (len(collectedTreasures) >= 3):
            break

    print("These are the treasures you collected: ")
    print(collectedTreasures)

    print("It took you " + str(numberOfTries) + " to collect all of those treasures. ")

main()