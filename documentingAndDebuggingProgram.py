#Kade Donohoue
#5/12/23
#Raise awareness in high schools about the impact of voting. 

def main():
    votingAge = 18
    name = input("What's your name?")
    age = int(input("How old are you?"))
    importantReason = input("Why is voting important to you?")

    print("Hello "+name+" you will be able to vote in "+ str(votingAge - age) +" years. You think voting is important because " + importantReason)

main()