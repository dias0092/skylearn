print("What deposit do you want?")
print("1. You have 10% interest every year, and at the end of each year, your interest rate increases by 5%. The currency of this deposit is Tenge ₸.")
print("2. You get 5% interest every month, but this deposit can only be open for 1 year. The currency of this deposit is Dollar $.")
answer = int(input("Your answer: "))

if answer == 1:
    print("Your balance for this deposit: ₸0")
    income = int(input("How much do you want to deposit: ₸"))
    print(f"Your balance is: ₸{income}")
    print("Below you have analysis if you deposit only 1 time at the beginning")
    incomeAfterYear1 = income + (income * 10) // 100
    incomeAfterYear2 = incomeAfterYear1 + (incomeAfterYear1 * 15) // 100
    incomeAfterYear3 = incomeAfterYear2 + (incomeAfterYear2 * 20) // 100
    incomeAfterYear4 = incomeAfterYear3 + (incomeAfterYear3 * 25) // 100
    incomeAfterYear5 = incomeAfterYear4 + (incomeAfterYear4 * 30) // 100
    print(f"After 1 year, you can have: ₸{incomeAfterYear1}")
    print(f"After 2 years, you can have: ₸{incomeAfterYear2}")
    print(f"After 3 years, you can have: ₸{incomeAfterYear3}")
    print(f"After 4 years, you can have: ₸{incomeAfterYear4}")
    print(f"After 5 years, you can have: ₸{incomeAfterYear5}")
elif answer == 2:
    print("Your balance for this deposit: $0")
    income = int(input("How much do you want to deposit: $"))
    print("Below you have analysis if you deposit only 1 time at the beginning")
    interest_rate = 5 / 100
    balance = income * (1 + interest_rate)**12
    print(f"After 1 year, you can have: ${balance}")
else:
    print("You entered the wrong answer, please try again")