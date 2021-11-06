# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from time import sleep
import sys
from os import system, name

# Credits: As per readme credits section - this clear terminal function
# is taken from the methods used by geeksforgeeks.org - see full details
# and links in credits section of readme
def clear():
    """
    Clears the terminal for formatting purposes
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

revenue = 1000000
revenue_delta = "     "
expenses = 700000
expense_delta = "     "
profits = revenue - expenses
profit_delta = "     "
shareholders = "Shareholders:      😐"
shareholder_delta = "  "
customers = "Customers:         😐"
customer_delta = "  "
employees = "Employees:         😐"
employee_delta = "  "


dashboard_0 = f"\n------------------------------------------------------------\n\
Financial Projections:         |     Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue} {revenue_delta}      |      {shareholders} {shareholder_delta}    \n\
Expenses:  €{expenses} {expense_delta}       |      {customers} {customer_delta}    \n\
Profits:   €{profits} {profit_delta}       |      {employees} {employee_delta}    \n\
------------------------------------------------------------\n"

print(dashboard_0)

input("\n[Press Enter To Begin]")

def question_1(revenue, revenue_delta, expenses, expense_delta, profits, profit_delta, shareholders, shareholder_delta, customers, customer_delta, employees, employee_delta, dashboard_0):
    
    clear()
    print(dashboard_0)
    scenario_1 = "\nScenario 1: You must decide at what level the selling price for \n\
    FictonalCorp's leading product should be set for the coming year:\n\
    \n    A. Increase Current Selling Price\n\
        B. Maintain Current Selling Price \n\
        C. Reduce Current Selling Price\n"
    print(scenario_1)
    while True:
        input1 = input("\nPlease Select an option - A, B or C: ").upper()
        if input1.upper() not in ('A', 'B', 'C'):
            print("Please Enter A Valid Choice - A, B or C")
        else:
            break
    scenario_1_answer_1 = "\nYou have chosen Option A\n \n- Increasing Selling Prices by ~5% has resulted in a decrease in projected\n\
    units sold, with customers choosing competitor alternatives\n\
    - Unfortunately overall Revenue projections have declined\n\
    - With expenses unchanged, profit projections have fallen as a result\n"
    scenario_1_answer_2 = "\nYou have chosen Option B\n \n- Maintaining Current Selling Prices has resulted in no change to projected\n\
    units sold\n\
    - Overall Revenue projections are unchanged\n\
    - With expenses flat, profit projections have remained static as a result\n"
    scenario_1_answer_3 = "\nYou have chosen Option C\n \n- Reducing Selling Prices by ~5% has resulted in an increase in projected\n\
    units sold, with several new customers interested\n\
    - Overall Revenue projections have increased as a result\n\
    - With expenses unchanged, profit projections have increased\n"
    if input1 == "A":
        
        revenue_delta = -50000
        revenue1 = revenue + revenue_delta
        expense_delta = 0
        expenses1 = expenses + expense_delta
        profit_delta = revenue_delta + expense_delta
        profits1 = revenue - expenses
        shareholders = "Shareholders:      🙁"
        shareholder_delta = -1
        customers = "Customers:         😐"
        customer_delta = ""
        employees = "Employees:         😐"
        employee_delta = ""

        dashboard_0 = f"\n------------------------------------------------------------\n\
Financial Projections:    |     Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue1} {revenue_delta}      |      {shareholders} {shareholder_delta}    \n\
Expenses:  €{expenses1} {expense_delta}       |      {customers} {customer_delta}    \n\
Profits:   €{profits1} {profit_delta}       |      {employees} {employee_delta}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta)}\n"
        clear()
        print(scenario_1_answer_1)
        print(dashboard_0)
        input("\nPress Enter To Proceed to Next Scenario")
    elif input1 == "B":
        clear()
        print(scenario_1_answer_2)
        print(dashboard_0)
        input("\nPress Enter To Proceed to Next Scenario")
    elif input1 == "C":
        revenue = 1050000
        profits = revenue - expenses
        shareholders = "Shareholders:      🙂"
        customers = "Customers:         😐"
        employees = "Employees:         😐"
        dashboard_0 = f"\n------------------------------------------------------------\n\
    Financial Projections:       |     Stakeholder Sentiment :  \n\
    ------------------------------------------------------------\n\
    Revenue:  €{revenue} (+€50000) |      {shareholders} (+1)  \n\
    Expenses: €{expenses}            |      {customers}     \n\
    Profits:  €{profits}  (+€50000) |      {employees}     \n\
    ------------------------------------------------------------\n\
                                                Total Points: +1\n"
        clear()
        print(scenario_1_answer_3)
        print(dashboard_0)
        input("\nPress Enter To Proceed to Next Scenario\n")
    print(revenue1)
    return revenue1, expenses1, profits1, shareholders, customers, employees, dashboard_0


question_1(revenue, revenue_delta, expenses, expense_delta, profits, profit_delta, shareholders, shareholder_delta, customers, customer_delta, employees, employee_delta, dashboard_0)

print(revenue1)