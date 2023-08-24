##Get the users name
user_name = input("Enter Your Name? ")

##print welcome message
print(f"Hello, {user_name}, Welcome to your Interest Calculator!" "\n"
     "We will determine the Total Interest paid overtime ")

##storing data 
total_debt = int(input("How much do you owe your car loan Ex. 45354?  "))
interest_rate = float(input("What is your interest rate Ex. 3.98?  "))
loan_term = int(input("How many years left do you have on your loan term Ex. 7?  "))



## Principal loan amount x interest rate x loan term = interest
interest = (float(total_debt * interest_rate/100 * loan_term))
##rounding interest
rounded_interest = round(interest, 2)
##currency format
formated_interest = "{:,}".format(rounded_interest)


print(f"Hello, {user_name}, Your total interest over the course of {loan_term} years is ${formated_interest}!" "\n"
      "Keep going, you're doing great :)")











""" 
Asking for multiple credit cards
number_credit_cards = 0

while True:
    try:
        ##Take and store total amount of credit cards
        number_credit_cards = int(input("How many credit cards do you have?" "\n" "5 CREDIT CARD MAX!"))
    if number_credit_cards >=1 and number_credit_cards <=5:
        

 """
