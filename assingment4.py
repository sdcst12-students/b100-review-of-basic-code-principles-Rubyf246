"""
### Assignment 4
#### Calculation of a debt repayment with recurring payments
This is the reverse of assignments 2 and 3

Calculate how long it will take to completely pay off a debt if regular payments are made.  Note that each year, the debt will increase by the amount of loan interest, but will decrease with youre recurring payment. 

Criteria:
Your program should ask the user for
* an initial debt
* the annual interest rate
* the annual payment
* the program will state how long it will take for the debt to be repaid.
* extra: Calculate the total amount of interest that is paid along with the debt repayment

Sample:
Joey takes a car loan to buy a new Tesla for $62000
The loan has an annual interest rate of .75% per month.  He makes monthly payments of $1000.
How many months will it take him to pay off the car.  How much interest has he paid in that time?

84 months
He will have paid 21711.60 in interest
"""

P= float(input("Enter the initial debt amount: "))
r= float(input("Enter the annual interest rate (in %): "))
t = float(input("Enter the annual payment amount: "))


yearinterest_rate = P / 100

years = 0 
total_interest_paid = 0.0  

while initial_debt > 0:

    interest = initial_debt * yearinterest_rate
    total_interest_paid += interest 
    initial_debt += interest  
    
    
    initial_debt -= t
    years += 1 
    
    if initial_debt < 0:
        initial_debt = 0


print(f"\nIt will take {years} years to pay off the debt.")
print(f"Total interest paid: {total_interest_paid:.2f}")