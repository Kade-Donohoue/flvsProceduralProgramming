#Kade Donohoue
#5/17/23
#Help with finding best shipping option for the user

def main():

    weight = int(input("How much does the package weigh? type in pounds rounded up."))
    budget = float(input("How much are you willing to spend?"))
    shippingDays = int(input("How long do you want shipping to take? type in days between 1 and 7"))

    weightCost = 1.5 * weight

    inBudget = True

    if (shippingDays <= 1):
        if budget >= (weightCost+15):
            print("You can get 1 day shipping which will fit your budget and how quickly you want to get your package. It will cost you $" + str(weightCost+15))
        else:
            print("to meet you desired shipday you would need to get 1 day shipping. that’s over your budget.")
            inBudget = False

    elif (shippingDays >= 1 and shippingDays <=5):
        if budget >= (weightCost+10):
            print("you can get standard shipping (1-5 days) which will fit your budget and is the closest to your desired shipping length. It will cost you $" + str(weightCost+10))
        else:
            print("to meet you desired ship day you would need to get standard (1-5 days) shipping. that’s over your budget. ")
            inBudget = False

    elif (shippingDays > 5):
        if budget >= (weightCost+5):
            print("you can get Slow shipping (5-7 days) which will fit your budget and is the closest to your desired shipping length. It will cost you $" + str(weightCost+5))
        else:
            print("to meet you desired ship day you would need to get Slow shipping (5-7 days)  but that’s over your budget. ")
            inBudget = False

    if (inBudget == False):
        if ((weightCost + 15) <= budget):
            print("but 1 day shipping fits your budget. It will cost you " + str(weightCost+15) )
        if ((weightCost + 10) <= budget):
            print("but standard shipping (1-5 days) fits your budget. It will cost you $" + str(weightCost+15) )
        if ((weightCost + 5) <= budget):
            print("but slow shipping (5-7 days) fits your budget. It will cost you $" + str(weightCost+10) )
        else:
            print("but no shipping options fit your budget.")
        

main()