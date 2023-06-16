#Kade Donohoue
#6/14/23
#Help HumanaTech decided where to provide life saving technology.

import math

def main():
    menu()

def menu():
    print('1.) Survey')
    print('2.) Research')
    print('3.) Average')
    print('4.) Quit')

    option = int(input('Choose an option. 1.) survey, 2.) research, 3.) average, 4.) quit'))
    if(option == 1):
        survey()
    elif(option == 2): 
        research()
    elif(option == 2): 
        average()

    if (option != 4):
        menu()    

def average(list):
    listAverage = sum(list) / len(list) 
    return listAverage

def survey():
    userMostNeed = input(' What countries do you think are most in need? Separated by a comma(,)')
    places = userMostNeed.split(',')

    #used to store how much a certain place needs aid
    priorityValue = []
    for place in places:
        comInf = input('Does ' + place + ' have communication infrastructure? yes or no')
        ldn = input("Is " + place + " on the UN's least developed nations list? yes or no")
        popDens = float(input('What is the population density of ' + place + '? in people per km²'))

        #adds points to calculate how important it is to help
        tempPriority = 0
        if (comInf.lower == 'no'):
            tempPriority += 100
        if (ldn.lower == 'yes'):
            tempPriority += 100
        if (popDens > 0):
            tempPriority += math.sqrt(popDens)

        priorityValue.append(tempPriority)

    print('The country that could use help the most is ' + places[priorityValue.index(max(priorityValue))]) #Gets the place with highest priority value and prints it
    print('The average importance value of the countries you listed is ' + str(average(priorityValue)) + ' while '+ places[priorityValue.index(max(priorityValue))] +' is at ' + str(max(priorityValue)))

def research():
    print('One of the biggest issues that prevent people from getting aid is a lack of communication infrastructure. It can prevent emergency services from even knowing about someone in need.')
    print('Also many factors are taking into account when determining poverty. Things like any income source, expenses, and educational assistance are considered. ')

main()
