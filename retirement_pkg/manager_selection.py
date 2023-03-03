def manager(pro):
    print("""Before you decide you are approached by a finanical advsior. 
She offers portolio management services for an asset-based fee. 
If you hire the advisor, you will pay 1% of your assets per year, 
but your allocation decisions will be made by a professional.\n""")
    print("""You are not sure, so you ask a friend, who tells you about 
life-cycle portfolios, an all-in-one investment option that 
offers you, in a single fund, a diversified portfolio with an 
asset allocation geared to the year in which you expect to 
retire. These portfolios incur management fees of 1.25% per year.\n""")
    while True:
        option = input("Would you like to choose an advisor or life-cycle portfolio? ").lower()
        if option == "yes" or option == "y":
            print("1. Financial Advisor")
            print("2. Life-Cycle Portfolio")
            while True:
                pro = input("Which option do you choose? ").lower()
                if pro == "1" or pro =="advisor" or pro == "financial advisor":
                    print("You have chosen to hire a financial advisor. They will allocate your portfolio and contact")
                    print("you with updates along the way. You will be able to fire the advisor if you decide.")
                    return pro
                elif pro =="2" or pro == "life-cycle portfolio" or pro == "lifecycle"  or pro == "life-cycle":
                    print("You have chosen a life-cycle portfolio. Your savings will be allocated based on your expected")
                    print("retirement age. You will recieve regular statements with updates on your account.")
                    return pro
                else:
                    print("Please enter 1 or 2.")
                    continue        
        elif option == "n" or option == "no":
            pro = "3"
            return pro
        else:
            print("Please enter yes or no.")
            continue
