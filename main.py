##Get the users name
user_name = input("Enter Your Name? ")

##print welcome message
print(f"Hello, {user_name}, Welcome to your Interest Calculator!" "\n"
      "We will determine the Total Interest paid overtime ")

total_debt = int(input("How much do you owe your car loan?"))
interest_rate = float(input("What is your interest rate?"))
loan_term = int(input("How many years left do you have on your loan term?"))

## Principal loan amount x interest rate x loan term = interest

interest = float(total_debt * interest_rate/100 * loan_term)

print(f"Hello, {user_name}, Your total interest over the course of {loan_term} years is ${interest}!" "\n"
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
