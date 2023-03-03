import random
#self-allocation function
def fund_allocation(funds):
    print("------------------------------------------------------------------------------------------")
    print("It is the beginning of the year, and you plan to hold your investments for the entire")
    print("year before making any changes. The investments are funds from the four major asset")
    print("classes: 1. Equities; 2. Bonds; 3. Real Assets; and, 4. Cash. The fund investments will ")
    print("be listed below and you will asked to choose the portfolio allocations. Choose wisely!")
    while True:
        total_allocation = 0
        funds[3]["Equity Fund"] = 0
        funds[3]["Bond Fund"] = 0
        funds[3]["Real Assets Fund"] = 0
        funds[3]["Money Market Fund"] = 0
        print(funds[3])
        for x in funds[3]:
            print("------------------------------------------------------------------------------------------")
            print("The", x, "has an average annual return of",funds[1][x], "and an annual standard deviation of", funds[2][x])
            print("Please enter a number between 0 and",str((100-total_allocation))+".")
            while True:
                y = int(input("What percent would you like to allocate to the " +x+ "? \n"))
                if y < 0:
                    print("Please enter a positive number.")
                elif y > 100:
                    print("Your allocation to the", x, "is greater than 100%.")
                elif total_allocation + y > 100:
                    print("Your total allocation is greater than 100%.")
                else:
                    total_allocation += y
                    funds[3][x] = y
                    print("You have allocated", str(y)+"% to the",str(x)+".")   
                    break
                if total_allocation == 100:
                    break
        return funds

#professional allocation function
def pro_allocation(age, retirement_age, funds):
    if retirement_age - age >= 30:
        funds[3]["Equity Fund"] = 80
        funds[3]["Bond Fund"] = 0
        funds[3]["Real Assets Fund"] = 20
        funds[3]["Money Market Fund"] = 0
    elif retirement_age - age < 30 and retirement_age - age >= 20:
        funds[3]["Equity Fund"] = 70
        funds[3]["Bond Fund"] = 20
        funds[3]["Real Assets Fund"] = 10
        funds[3]["Money Market Fund"] = 0
    elif retirement_age - age < 20 and retirement_age - age >= 10:
        funds[3]["Equity Fund"] = 50
        funds[3]["Bond Fund"] = 40
        funds[3]["Real Assets Fund"] = 10
        funds[3]["Money Market Fund"] = 0
    elif retirement_age - age < 10 and retirement_age - age >= 5:
        funds[3]["Equity Fund"] = 20
        funds[3]["Bond Fund"] = 75
        funds[3]["Real Assets Fund"] = 5
        funds[3]["Money Market Fund"] = 0
    else:
        funds[3]["Equity Fund"] = 10
        funds[3]["Bond Fund"] = 75
        funds[3]["Real Assets Fund"] = 5
        funds[3]["Money Market Fund"] = 10
    return funds

# to be used if comparison portfolio is added
def compare_allocation(funds):
    funds[3]["Equity Fund"] = random.randint(0,101)
    funds[3]["Bond Fund"] = random.randint(0, 100-funds[3]["Equity Fund"])
    funds[3]["Real Assets Fund"] = random.randint(0,100-funds[3]["Equity Fund"]-funds[3]["Bond Fund"])
    remaining = 100 - funds[3]["Equity Fund"]-funds[3]["Bond Index"] - funds[3]["Real Assets Fund"]
    funds[3]["Money Market Fund"] = random.randint(0, remaining)
    return funds