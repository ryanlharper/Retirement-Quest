import random

def random_events(value, age):
    random_negative_events = ["slip on ice, end up in the hospital","get fined by the IRS","have a child kidnapped","have a family member die","have an earthquake detroy your garage","lose a lawsuit"]
    random_positive_events = ["get a bonus at work","hit the lottery","find money in the subway","receive an inheritance","win a settlement"]
    event = random.randint(1,2)
    random_positive = random.randint(5000,15000)
    if event % 2 == 0:
        print("---------------------------------------------------------------------------")
        print("You are", age ,"and your account is now $"+str(int(value))+". You", random.choice(random_positive_events), "and you receive $"+ str(random_positive)+".\n")
        print("1. Yes")
        print("2. No")
        while True:
            choice = input("Would you like to deposit the money into your retirement account? ").lower()
            if choice == "1" or choice == "yes" or choice == "y":
                value = int(value + random_positive)
                print("Your account is now worth $" + str(value)+".\n")
            elif choice == "2" or choice == "no" or choice == "n":
                print("Your account balance remains at $"+str(value)+".\n")
            else:
                print("Please choose Yes or No.")
                continue 
            print("---------------------------------------------------------------------------")    
            return value
    else:
        print("---------------------------------------------------------------------------")
        print("You are", age ,"and your account is now $"+str(int(value))+". You",random.choice(random_negative_events), "and you must pay $"+ str(random_positive)+".\n")
        value = int(value - random_positive)
        if value < 0:
            print("You have lost all of your savings and must repay your debt.")
            print("Please play again soon!")
            exit()
        elif value == 0:
            print("You have lost all of your savings and must start from scratch.")
            print("Please play again soon!")
            exit()
        else:
            print("Your account is now worth $" +str(value)+".\n")
            print("---------------------------------------------------------------------------")
        return value