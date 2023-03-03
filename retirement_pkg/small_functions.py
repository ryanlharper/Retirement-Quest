import random

def target(target_return, value, goal, retirement_age, age, contribution):
    target_return = int(float(((goal/(value+(contribution*(retirement_age-age))))**(1/(retirement_age-age)))-1)*100)
    print("---------------------------------------------------------------------------------------------------------")
    print("You must decide how to manage your $" + str(int(value)), "investment account to meet your goal. You feel secure retiring")
    print("with $"+str(goal) , "in", retirement_age-age, "years. To meet this goal, you need an annualized return of", str(target_return)+"%","over the next" , retirement_age - age , "years.")
    print("---------------------------------------------------------------------------------------------------------")
    return target_return

def value(value, performance, pro, contribution):
    if pro == "1":
        value = value*(1+(performance/100)) - (value * .01) + contribution
    elif pro == "2":
        value = value*(1+(performance/100)) - (value * .0125) + contribution
    elif pro == "3":
        value = value*(1+(performance/100)) + contribution
    return value  

def death(age, value):
    death_reason = ["fell down the stairs","were in a plane crash" , "had a heart attack while jogging", "were mistaken for a mobster","were in a one hundred car pile up","were helping an old lady across the street, were hit by a bus"]
    death_reason = random.choice(death_reason)
    print("You", death_reason, "and died unexpectedly at", str(age)+". The $" + str(int(value)), "you saved will go to your beneficiaries.")
    print("Please play again.")
    exit()

def payments(value, age):
    death_age = random. randint(age+1, 105)
    if death_age > 79:
        print("Unfortunately, you lived to be", death_age, "and payments ended when you turned 80.")
        print("Hopefully you saved some of your payments during retirement or had family to rely on.")
        print("--------------------------------------------------------------------------------------")
        print("Please play again.")
        exit()
    else:
        payment = int(value) / ((79 - age)*12)
        remainder = int(value) - int((payment)*((death_age-age)*12))
        print("You died at",death_age,"years of age and left $"+str(remainder),"to your beneficaries.")
        print("--------------------------------------------------------------------------------------")
        print("Please play again.")
        exit()

def retire_choice(age, value):
    pay = int(value / ((79 - age)*12))
    print("If you retire, you will receive monthly, pre-tax")
    print("payments of approximately $" +str(pay), "until you are 79.\n")
