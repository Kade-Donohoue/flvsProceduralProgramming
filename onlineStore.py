#Kade Donohoue
#5/15/23
#incentivizes a customer to spend $200 or more

def main():
    print("**************************************")
    print("Welcome to the online store of things!")
    print("**************************************")

    budget = int(input("What is your budget?"))
    amountUntilGift = 200 - budget

    print("Your budget is $" + str(budget))

    #Check if user qualifies for a gift and tell them how far off they are. 
    if (amountUntilGift > 0 ):
        print("If you spend $" + str(amountUntilGift) + " more than you can get a free gift!")
    else:
        print("You qualify for a free gift")

    
    #Suggest a product to the user based on budget
    if (budget <= 1):
        if (budget < 0):
            print("Sorry We cant pay you.")
        else:
            print("We dont have anything within your budget.")
    elif (budget >1 and budget <3):
        print("We recommend a candy bar.")
    elif (budget >=3 and budget <50):
        print("We recommend a sweater")
    elif (budget >=50 and budget <100):
        print("We recommend a video game")
    elif (budget >=100 and budget <150):
        print("We recommend a calculator")
    elif (budget >=150):
        print("We recommend a table")


    print("**************************************")
    print("Thanks for shopping!")
    print("**************************************")

main()