import random
from retirement_pkg import allocation, manager_selection, small_functions, probabilities, mgr_prob, random_events

target_return = 0
pro = ""
funds = {1: {"Equity Fund": 12.32, "Bond Fund": 3.67, "Real Assets Fund": 14.04, "Money Market Fund": 1.15}, 2: {"Equity Fund": 19.53, "Bond Fund": 2.25, "Real Assets Fund": 8.72, "Money Market Fund": 0.15}, 3: {"Equity Fund": 0, "Bond Fund": 0, "Real Assets Fund": 0, "Money Market Fund": 0}}

# setup the game
print("")
print("== Welcome to Retirement Quest! ==")
print(" An engaging retirement calculator.\n")
print("Your goal is to make investment decisions and meet your retirement goal.")

while True:
    option = input("Would you like to play the game? \n").lower()
    if option == "1" or option == "yes" or option == "y":
        name = input("What is your name? \n")
        print("------------------------------------------------------------")
        print("Hi", name+"! Welcome to the game. You will be asked a series")
        print("of questions. Your answers will help determine the outcome.")
        print("However, there will be several random events along the way")
        print("that may help or hinder your progress. Good Luck", name+"!")
        print("------------------------------------------------------------")
        while True:    
            while True:
                try:
                    age = int(input("How old are you? \n"))
                    break
                except ValueError:
                    print("Age must be only numerals.")
                    continue
            if age <= 0:
                print("You must be born to play the game.")
                exit()
            elif age >= 100:
                print("You should probably retire now!")
                exit()
            else:
                break
        while True:
            while True:
                try:
                    retirement_age = int(input("At what age would you like to retire? \n"))
                    break
                except ValueError:
                    print("Retirement age must be only numerals.")
                    continue
            if retirement_age <= age:
                print("Looks like you have already retired.")
                exit()
            elif retirement_age > 99:
                print("For reasonability considerations, please choose a retirement age below 100.")
            else:
                break
        while True:
            while True:
                try:
                    value = int(input("How much do have you saved for retirement? \n"))
                    break
                except ValueError:
                    print("Please enter numerals only.")
                    continue
            if value <= 0:
                print("Your savings must be greater than zero.")
                exit()
            else:
                break
        while True:
            while True:
                try:
                    contribution = int(input("What is your annual income? \n"))
                    break
                except ValueError:
                    print("Contribution must be a numeral.")
                    continue
            if contribution < 0:
                print("Please enter zero or a positive number.")
                continue
            else:
                while True:
                    try:
                        option = int(input("What percent of your income can you afford to save? \n"))
                        break
                    except ValueError:
                        print("Percent must be entered as a numeral.")
                        continue
                if option < 0 or option > 100:
                    print("Please enter a number between 0 and 100.")
                    continue
                else:
                    contribution = contribution * (option/100)
                    break
        while True:
            while True:
                try:
                    goal = int(input("How much do you need to have to retire securely? \n"))
                    break
                except ValueError:
                    print("Retirement goal must be enter as a numeral.")
                    continue
            if goal <= value:
                print("You already have your savings goal met.")
                exit()
            else:
                death_age = 79
                if death_age <= retirement_age:
                    pay = int(goal / (10*12))
                    print("A monthly, pre-tax payment of approximately $"+str(pay))
                    print("will be paid for 10 years upon your retirement.\n")
                else:
                    pay = int(goal / ((death_age - retirement_age)*12))
                    print("Based on the actuarial life table, this goal will provide monthly,")
                    print("pre-tax payments of approximately $" +str(pay), "upon retirement.\n")
                option = input("Will this payment meet your needs? \n").lower()
                if option == "yes" or option == "y":
                    break
                elif option == "no" or option == "n":
                    continue
                else:
                    print("Please try again.")

        small_functions.target(target_return, value, goal, retirement_age, age, contribution)
        break
    elif option == "2" or option == "no" or option == "n":
        print("Please come back another time.")
        exit()
    else:
        print("Please enter Yes or No.\n")

# inital allocation selection
pro = manager_selection.manager(pro)
if pro == "1" or pro == "2":
    allocation.pro_allocation(age, retirement_age, funds)
else:
    allocation.fund_allocation(funds)

#game-play loop
while True:
    while True:
        if retirement_age - age <= 0 :
            print("You reached your retirement age!")
            small_functions.retire_choice(age, value)
            option = input("Would you like to retire? ")
            if option == "yes" or option == "y":
                small_functions.payments(value, age)
            elif option == "no" or option == "n":
                while True:
                    try:
                        retirement_age = int(input("Please update your retirement age. \n"))
                        break
                    except ValueError:
                        print("Retirement age must be only numerals.")
                        continue
                if retirement_age <= age:
                    print("Looks like you have already retired.")
                    exit()
                elif retirement_age > 99:
                    print("For reasonability considerations, please choose a retirement age below 100.")
                else:
                    break
            else:
                print("Please enter yes or no.")
                continue
        else:
            break
    if goal > value:
        age += 1        
        if pro == "1":
            performance = mgr_prob.mgr_performance_calc(funds)
            value = small_functions.value(value, performance, pro, contribution)
            allocation.pro_allocation(age, retirement_age, funds)
        elif pro == "2":
            performance = probabilities.performance_calc(funds)
            value = small_functions.value(value, performance, pro, contribution)
            allocation.pro_allocation(age, retirement_age, funds)
        else:
            performance = probabilities.performance_calc(funds)
            value = small_functions.value(value, performance, pro, contribution)
        while True:
            if random.randint(1, 10) == random.randint(1, 10):
                value = random_events.random_events(value, age)
            else:
                if random.randint(1,3) == random.randint(1,3):
                    if pro != "1":
                        print("-----------------------------------------------------------------------------------------------------")
                        print("You check your account because you are thinking about making changes. You are", age, "and your account")
                        option = input("is now worth $" +str(int(value))+". Would you like to change your allocations? ").lower()
                    else:
                        print("-------------------------------------------------------------------------------------------------")
                        print("Your advisor calls you to check in. You are", age, "and your account is now worth $" +str(int(value))+".")   
                        option = input("Would you like to fire your advisor? ").lower()                     
                    while True:
                        if option == "y" or option == "yes":
                            small_functions.target(target_return, value, goal, retirement_age, age, contribution)    
                            pro = manager_selection.manager(pro)
                            if pro == "1" or pro == "2":
                                allocation.pro_allocation(age, retirement_age, funds)
                                break
                            else:
                                allocation.fund_allocation(funds)   
                                break
                        elif option == "n" or option == "no":
                                break
                        else:
                            print("Please enter yes or no.")
                            continue   
                    break             
            break
        while True:
            death_age = random.randint(59, 104)
            if death_age <= age:
                small_functions.death(age, value)
            else:
                break
    elif value >= goal:
        print("--------------------------------------------------------------------------------------")
        print("At",age, "you met your goal early and can retire early.")
        small_functions.retire_choice(age, value)
        option = input("Would you like to retire early? ")
        if option == "yes" or option == "y":
            small_functions.payments(value, age)
        elif option == "no" or option == "n":
            while True:
                try:
                    goal = int(input("How much do you now need to retire securely? \n"))
                    break
                except ValueError:
                    print("Retirement goal must be entered as a numeral.")
                    continue
            if goal <= value:
                print("You already have your savings goal met.")
                small_functions.payments(value, age)
           



            
# add more uses to "name" variable
# factor in comparison portfolio 
# factor in social security
# factor in continuing investment in retirement 
# link to yfinance for portfolio construction 


