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

def emoji_assignment(delta):
    """
    Assigns emoji to dashboard categories based on stakehodler sentiment score
    """
    if delta >= 2:
        emoji = "😀"
    elif delta == 1:
        emoji = "🙂"
    elif delta == 0:
        emoji = "😐"
    elif delta == -1:
        emoji = "🙁"
    elif delta <= -2:
        emoji = "😠"

    return emoji

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
        revenue_delta1 = -50000
        revenue1 = revenue + revenue_delta1
        expense_delta1 = 0
        try:
            expenses1 = expenses + expense_delta
        except TypeError:
            expenses1 = expenses 
        profit_delta1 = revenue_delta1 - expense_delta1
        profits1 = revenue1 - expenses1        
        shareholder_delta1 = -1
        shareholders1 = "Shareholders:      " + emoji_assignment(shareholder_delta1)
        customer_delta1 = 0
        customers1 = "Customers:         " + emoji_assignment(customer_delta1)
        employee_delta1 = 0
        employees1 = "Employees:         " + emoji_assignment(employee_delta1)        

        dashboard_1 = f"\n------------------------------------------------------------\n\
Financial Projections:     |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue1} €{revenue_delta1}  |   {shareholders1}  {shareholder_delta1}    \n\
Expenses:  €{expenses1} €{expense_delta1}       |   {customers1}  {customer_delta1}    \n\
Profits:   €{profits1} €{profit_delta1}  |   {employees1}  {employee_delta1}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta1 + customer_delta1 + employee_delta1)}\n"
        clear()
        print(scenario_1_answer_1)
        print(dashboard_1)
        input("\nPress Enter To Proceed to Next Scenario")
    
    elif input1 == "B":
        revenue_delta1 = 0
        revenue1 = revenue + revenue_delta1
        expense_delta1 = 0
        try:
            expenses1 = expenses + expense_delta
        except TypeError:
            expenses1 = expenses 
        profit_delta1 = revenue_delta1 - expense_delta1
        profits1 = revenue1 - expenses1
        shareholder_delta1 = 0
        shareholders1 = "Shareholders:      " + emoji_assignment(shareholder_delta1)
        customer_delta1 = 0
        customers1 = "Customers:         " + emoji_assignment(customer_delta1)
        employee_delta1 = 0
        employees1 = "Employees:         " + emoji_assignment(employee_delta1)

        dashboard_1 = f"\n------------------------------------------------------------\n\
Financial Projections:     |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue1} €{revenue_delta1}     |    {shareholders1} {shareholder_delta1}    \n\
Expenses:  €{expenses1} €{expense_delta1}      |    {customers1} {customer_delta1}    \n\
Profits:   €{profits1} €{profit_delta1}      |    {employees1} {employee_delta1}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta1 + customer_delta1 + employee_delta1)}\n"
        clear()
        print(scenario_1_answer_2)
        print(dashboard_1)
        input("\nPress Enter To Proceed to Next Scenario")

    elif input1 == "C":
        revenue_delta1 = 50000
        revenue1 = revenue + revenue_delta1
        expense_delta1 = 0
        try:
            expenses1 = expenses + expense_delta
        except TypeError:
            expenses1 = expenses 
        profit_delta1 = revenue_delta1 - expense_delta1
        profits1 = revenue1 - expenses1
        shareholder_delta1 = 1
        shareholders1 = "Shareholders:      " + emoji_assignment(shareholder_delta1)
        customer_delta1 = 0
        customers1 = "Customers:         " + emoji_assignment(customer_delta1)
        employee_delta1 = 0
        employees1 = "Employees:         " + emoji_assignment(employee_delta1)

        dashboard_1 = f"\n------------------------------------------------------------\n\
Financial Projections:      |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue1} €{revenue_delta1}  |   {shareholders1}  {shareholder_delta1}    \n\
Expenses:  €{expenses1} €{expense_delta1}       |   {customers1}  {customer_delta1}    \n\
Profits:   €{profits1} €{profit_delta1}   |   {employees1}  {employee_delta1}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta1 + customer_delta1 + employee_delta1)}\n"
        clear()
        print(scenario_1_answer_3)
        print(dashboard_1)
        input("\nPress Enter To Proceed to Next Scenario\n")
    
    return revenue1, revenue_delta1, expenses1, expense_delta1, profits1, profit_delta1, shareholders1, shareholder_delta1, customers1, customer_delta1, employees1, employee_delta1, dashboard_1

revenue1, revenue_delta1, expenses1, expense_delta1, profits1, profit_delta1, shareholders1, shareholder_delta1, customers1, customer_delta1, employees1, employee_delta1, dashboard_1 = question_1(revenue, revenue_delta, expenses, expense_delta, profits, profit_delta, shareholders, shareholder_delta, customers, customer_delta, employees, employee_delta, dashboard_0)

# print(revenue1, revenue_delta1, expenses1, expense_delta1, profits1, profit_delta1, shareholders1, shareholder_delta1, customers1, customer_delta1, employees1, employee_delta1)
# print(dashboard_1)

def question_2(revenue1, revenue_delta1, expenses1, expense_delta1, profits1, profit_delta1, shareholders1, shareholder_delta1, customers1, customer_delta1, employees1, employee_delta1, dashboard_1):
    
    clear()
    print(dashboard_1)
    scenario_2 = "\nScenario 2: You must decide at what level the marketing budget \n\
    should be set for the coming year:\n\
    \n    A. Increase Marketing Expenditure \n\
    B. Maintain Marketing Expenditure \n\
    C. Decrease Marketing Expenditure \n"
    print(scenario_2)
    while True:
        input1 = input("\nPlease Select an option - A, B or C: ").upper()
        if input1.upper() not in ('A', 'B', 'C'):
            print("Please Enter A Valid Choice - A, B or C")
        else:
            break
    scenario_2_answer_1 = "\nYou have chosen Option A\n \n- Increasing the Marketing Budget by ~5% has resulted in an increase in projected\n\
    units sold, with increasing customer interest\n\
    - Yearly Revenue projection increases run ahead of equivalent expenditure increase projections\n\
    - Profit projections have increased as a result\n"
    scenario_2_answer_2 = "\nYou have chosen Option B\n \n- Retaining current marketing expenditure levels has resulted in flat projected\n\
    unit sales\n\
    - Yearly Revenue projections remain unchanged as a result\n\
    - With expenditure forecasts unchanged, Profit projections remained static\n"
    scenario_2_answer_3 = "\nYou have chosen Option C\n \n- Decreasing the Marketing Budget by ~5% has resulted in an decrease in projected\n\
    units sold, with cusotmers choosing competitor alternatives\n\
    - Yearly Revenue projection decreases are exceeding the equivalent reductions in expenditure projections\n\
    - Profit projections have decreased as a result\n"

    
    if input1 == "A":        
        revenue_delta2 = 100000
        revenue2 = revenue1 + revenue_delta2
        expense_delta2 = 50000
        expenses2 = expenses1 + expense_delta2
        profit_delta2 = revenue_delta2 - expense_delta2
        profits2 = revenue2 - expenses2
        shareholder_delta2 = shareholder_delta1 + 1
        shareholders2 = "Shareholders:      " + emoji_assignment(shareholder_delta2)
        customer_delta2 = customer_delta1 + 1
        customers2 = "Customers:         " + emoji_assignment(customer_delta2)
        employee_delta2 = 0
        employees2 = "Employees:         " + emoji_assignment(employee_delta2)
        

        dashboard_2 = f"\n------------------------------------------------------------\n\
Financial Projections:      |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue2} €{revenue_delta2} |   {shareholders2}  {shareholder_delta2}    \n\
Expenses:  €{expenses2} €{expense_delta2}   |   {customers2}  {customer_delta2}    \n\
Profits:   €{profits2} €{profit_delta2}  |   {employees2}  {employee_delta2}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta2 + customer_delta2 + employee_delta2)}\n"
        clear()
        print(scenario_2_answer_1)
        print(dashboard_2)
        input("\nPress Enter To Proceed to Next Scenario")
    
    elif input1 == "B":
        revenue_delta2 = 0
        revenue2 = revenue1 + revenue_delta2
        expense_delta2 = 0
        expenses2 = expenses1 + expense_delta2
        profit_delta2 = revenue_delta2 - expense_delta2
        profits2 = revenue2 - expenses2
        shareholder_delta2 = shareholder_delta1 + 0
        shareholders2 = shareholders1
        customer_delta2 = customer_delta1 + 0
        customers2 = customers1
        employee_delta2 = 0
        employees2 = employees1        

        dashboard_2 = f"\n------------------------------------------------------------\n\
Financial Projections:   |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue2} €{revenue_delta2}  |   {shareholders2}  {shareholder_delta2}    \n\
Expenses:  €{expenses2} €{expense_delta2}  |   {customers2}  {customer_delta2}    \n\
Profits:   €{profits2} €{profit_delta2}  |   {employees2}  {employee_delta2}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta2 + customer_delta2 + employee_delta2)}\n"
        clear()
        print(scenario_2_answer_2)
        print(dashboard_2)
        input("\nPress Enter To Proceed to Next Scenario")

    elif input1 == "C":
        revenue_delta2 = -50000
        revenue2 = revenue1 + revenue_delta2
        expense_delta2 = -50000
        expenses2 = expenses1 + expense_delta2
        profit_delta2 = revenue_delta2 - expense_delta2
        profits2 = revenue2 - expenses2
        shareholder_delta2 = shareholder_delta1 - 1
        shareholders2 = "Shareholders:      " + emoji_assignment(shareholder_delta2)
        customer_delta2 = customer_delta1 - 1
        customers2 = "Customers:         " + emoji_assignment(customer_delta2)
        employee_delta2 = 0
        employees2 = "Employees:         " + emoji_assignment(employee_delta2)        

        dashboard_2 = f"\n------------------------------------------------------------\n\
Financial Projections:     |    Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue2} €{revenue_delta2} |   {shareholders2}  {shareholder_delta2}    \n\
Expenses:  €{expenses2} €{expense_delta2}  |   {customers2}  {customer_delta2}    \n\
Profits:   €{profits2} €{profit_delta2}     |   {employees2}  {employee_delta2}    \n\
------------------------------------------------------------\n\
                                            Total Points: {(shareholder_delta2 + customer_delta2 + employee_delta2)}\n"
        clear()
        print(scenario_2_answer_3)
        print(dashboard_2)
        input("\nPress Enter To Proceed to Next Scenario")
    
    return revenue2, revenue_delta2, expenses2, expense_delta2, profits2, profit_delta2, shareholders2, shareholder_delta2, customers2, customer_delta2, employees2, employee_delta2, dashboard_2

revenue2, revenue_delta2, expenses2, expense_delta2, profits2, profit_delta2, shareholders2, shareholder_delta2, customers2, customer_delta2, employees2, employee_delta2, dashboard_2 = question_2(revenue1, revenue_delta1, expenses1, expense_delta1, profits1, profit_delta1, shareholders1, shareholder_delta1, customers1, customer_delta1, employees1, employee_delta1, dashboard_1)



