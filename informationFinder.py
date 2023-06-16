#Kade Donohoue
#6/6/23
#Find player information based on csv file

import csv

def main():
    while True:
        print("****************************************************************")
        print("1.) Search if a pre-registered player appears in the list or not")
        print("2.) Find the number of a specific player")
        print("3.) Print a list of players and their information")
        print("4.) quit")

        choice = input("What option? 1, 2, 3, or 4")
        with open("battle_royale.csv") as csvfile:
            readCSV = csv.reader(csvfile,delimiter=',')
            if choice == "1": 
                findPlayer(readCSV)
            elif choice == "2": 
                findNumber(readCSV)
            elif choice == "3": 
                printAll(readCSV)
            else: 
                break

def findPlayer(CSVFile):
    userName=input("What is the players Name?")
    found = False

    #finds if player name is either on avatar Name or player name and prints out if they are
    for row in CSVFile:
        if (row[0] == userName or row[1] == userName):
            print(userName + " Is Registered. ")
            found = True
    if not found:
        print("They are not registered")

def findNumber(CSVFile):
    userName=input("What is the players Name?")
    found = False

    #finds if player name is either on avatar Name or player name and prints their number if they are
    for row in CSVFile:
        if (row[0] == userName or row[1] == userName):
            print(userName + "'s number is " + str(row[2]))
            found = True
    if not found:
        print("They are not registered")
            

def printAll(CSVFile):
    for row in CSVFile:

        #prints all player information
        if row[0] != "Avatar Name":
            print(row)

main()