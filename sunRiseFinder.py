#Kade Donohoue
#5/30/23
#Find the day that the sun rises at the time the user asks. 

import csv

def main():
    print("Welcome to sunrise finder where you can find all the days the sun is up before a certain time. This will help with deciding the best day to start your travel!")

    time = int(input("What time do you need to sun to rise at? EX: write 6:30 as 630."))

    days = []
    months = []

    with open("sun_data.csv") as csvfile:
        readCSV = csv.reader(csvfile,delimiter=',')
        
        for row in readCSV:

            #find header and store as titles
            for i in range(len(row)):
                if (row[i] == "Date"):
                    titles = row
                    break

                #check if sun will rise before user inputed time
                if (int(row[i]) <= time and int(row[i]) > 30):

                    #add date to arrays
                    days.append(row[0])
                    months.append(titles[i])

    #print out dates that have been found
    if (len(days) >= 1):
        for i in range(len(days)):
            print("On " + str(months[i]) + " " + str(days[i]) + " The sun will rise before " + str(time))
    else: 
        print("There is no days the sun will rise before " + str(time))
        #go back to beginging 
        repeat = input("Do you want to try a different time? yes or no")
        if (repeat == "yes" or repeat == "Yes"):
            main()



main()