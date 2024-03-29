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

def main_menu():
    print("\n----------------------------------------------------------------------")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                   W E L C O M E                                    |")
    print("|                                                                    |")
    print("|                       T O                                          |")
    print("|                                                                    |")
    print("|                         P Y T H O N                                |")
    print("|                                                                    |")
    print("|                            T E X T                                 |")
    print("|                                                                    |")
    print("|                               A D V E N T U R E                    |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                     [ PRESS ENTER TO BEGIN ]                       |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("----------------------------------------------------------------------")
    input()
    clear()

main_menu()

intro = f"- The Year is 2021...\n- FictionalCorp have hired you as their new CEO\
\n- You have been tasked with improving their performance on three fronts:\n\
    \n1. Shareholder Sentiment\
    \n2. Customer Confidence\
    \n3. Employee Engagement\n\
    \n- You will receive one point for each improvement in stakeholder status\
    \n- You will lose one point for each decline in stakeholder status\n\
    \n- Navigate the following series of business decisions, and their respective\
    \nstakeholder impacts\n\
    \n- Your performance will be displayed on a dashboard in the format below:\n" 



revenue = 1000000
expenses = 700000
profits = revenue - expenses
shareholders = "Shareholders:      😐"
customers = "Customers:         😐"
employees = "Employees:         😐"

for letter in intro:
    sleep(0.001) 
    sys.stdout.write(letter)
    sys.stdout.flush()

dashboard_0 = f"\n------------------------------------------------------------\n\
Financial Projections:     |     Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue}       |      {shareholders}     \n\
Expenses:  €{expenses}        |      {customers}     \n\
Profits:   €{profits}        |      {employees}     \n\
------------------------------------------------------------\n"

for letter in dashboard_0:
    sleep(0.001) 
    sys.stdout.write(letter)
    sys.stdout.flush()

input("\n[Press Enter To Begin]")

clear()

for letter in dashboard_0:
    sleep(0.001) 
    sys.stdout.write(letter)
    sys.stdout.flush()

scenario_1 = "\nScenario 1: You must decide at what level the selling price for \n\
FictonalCorp's leading product should be set for the coming year:\n\
\n    A. Increase Current Selling Price\n\
    B. Maintain Current Selling Price \n\
    C. Reduce Current Selling Price\n"

for letter in scenario_1:
    sleep(0.001) 
    sys.stdout.write(letter)
    sys.stdout.flush()

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
    revenue = 950000
    profits = revenue - expenses
    shareholders = "Shareholders:      🙁"
    customers = "Customers:         😐"
    employees = "Employees:         😐"
    dashboard_0 = f"\n------------------------------------------------------------\n\
Financial Projections:       |     Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:  €{revenue} (-€50000)  |      {shareholders} {(-1)}  \n\
Expenses: €{expenses}            |      {customers}     \n\
Profits:  €{profits} (-€50000)  |      {employees}     \n\
------------------------------------------------------------\n\
                                            Total Points: -1\n"
    clear()
    for letter in scenario_1_answer_1:
        sleep(0.01) 
        sys.stdout.write(letter)
        sys.stdout.flush()
    for letter in dashboard_0:
        sleep(0.0001) 
        sys.stdout.write(letter)
        sys.stdout.flush()
    input("\nPress Enter To Proceed to Next Scenario")

elif input1 == "B":
    clear()
    for letter in scenario_1_answer_2:
        sleep(0.0001) 
        sys.stdout.write(letter)
        sys.stdout.flush()
    for letter in dashboard_0:
        sleep(0.001) 
        sys.stdout.write(letter)
        sys.stdout.flush()
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
    for letter in scenario_1_answer_3:
        sleep(0.0001) 
        sys.stdout.write(letter)
        sys.stdout.flush()
    for letter in dashboard_0:
        sleep(0.001) 
        sys.stdout.write(letter)
        sys.stdout.flush()
    input("\nPress Enter To Proceed to Next Scenario\n")




clear()
for letter in dashboard_0:
    sleep(0.001) 
    sys.stdout.write(letter)
    sys.stdout.flush()

scenario_2 = "\nScenario 2: You must decide at what level the marketing budget \n\
should be set for the coming year:\n\
\n    A. Increase Marketing Expenditure \n\
    B. Maintain Marketing Expenditure \n\
    C. Decrease Marketing Expenditure \n"

for letter in scenario_2:
    sleep(0.001) 
    sys.stdout.write(letter)
    sys.stdout.flush()

while True:
    input2 = input("\nPlease Select an option - A, B or C: ").upper()
    if input2.upper() not in ('A', 'B', 'C'):
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


if input2 == "A":
    revenue1 = revenue + 100000
    profits = revenue - expenses
    shareholders = "Shareholders:      🙁"
    customers = "Customers:         😐"
    employees = "Employees:         😐"
    dashboard_0 = f"\n------------------------------------------------------------\n\
Financial Projections:       |     Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:  €{revenue1} (-€50000)  |      {shareholders} {(-1)}  \n\
Expenses: €{expenses}            |      {customers}     \n\
Profits:  €{profits} (-€50000)  |      {employees}     \n\
------------------------------------------------------------\n\
                                            Total Points: -1\n"
    clear()
    for letter in scenario_2_answer_1:
        sleep(0.01) 
        sys.stdout.write(letter)
        sys.stdout.flush()
    for letter in dashboard_0:
        sleep(0.0001) 
        sys.stdout.write(letter)
        sys.stdout.flush()
    input("\nPress Enter To Proceed to Next Scenario")

elif input2 == "B":
    clear()
    for letter in scenario_2_answer_2:
        sleep(0.0001) 
        sys.stdout.write(letter)
        sys.stdout.flush()
    for letter in dashboard_0:
        sleep(0.001) 
        sys.stdout.write(letter)
        sys.stdout.flush()
    input("\nPress Enter To Proceed to Next Scenario")

elif input2 == "C":
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
    for letter in scenario_2_answer_3:
        sleep(0.0001) 
        sys.stdout.write(letter)
        sys.stdout.flush()
    for letter in dashboard_0:
        sleep(0.001) 
        sys.stdout.write(letter)
        sys.stdout.flush()
    input("\nPress Enter To Proceed to Next Scenario\n")

