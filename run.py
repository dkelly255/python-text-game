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


string = f"- The Year is 2021...\n\n- FictionalCorp have hired you as their new CEO\
\n- You have been tasked with improving their performance on three fronts\n\
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

for letter in string:
    sleep(0.001) 
    sys.stdout.write(letter)
    sys.stdout.flush()

string1 = f"------------------------------------------------------------\n\
Financial Projections:     |     Stakeholder Sentiment :  \n\
------------------------------------------------------------\n\
Revenue:   €{revenue}       |      {shareholders}     \n\
Expenses:  €{expenses}        |      {customers}     \n\
Profits:   €{profits}        |      {employees}     \n\
------------------------------------------------------------\n"

for letter in string1:
    sleep(0.0035) 
    sys.stdout.write(letter)
    sys.stdout.flush()

input("\n[Press Enter To Begin]")

clear()

for letter in string1:
    sleep(0.001) 
    sys.stdout.write(letter)
    sys.stdout.flush()

string2 = "\nScenario 1: You must decide at what level the selling price for \n\
FictonalCorp's leading product should be set for the coming year:\n\
\n    A. Increase Current Selling Price\n\
    B. Maintain Current Selling Price \n\
    C. Reduce Current Selling Price\n"

for letter in string2:
    sleep(0.02) 
    sys.stdout.write(letter)
    sys.stdout.flush()

answer1 = input("\nPlease Select an option - A, B or C: ").upper()

string3 = "You have chosen Option A\n - Increasing Selling Prices by ~5% has resulted in a decrease in projected\n\
units sold, with customers choosing competitor alternatives,\n\
overall Revenue projections have declined\n"
string4 = "You have chosen Option B\n - Revenue is unchanged\n"
string5 = "You have chosen Option C\n - Revenue has increased\n"

if answer1 == "A":
    clear()
    print(revenue)
    revenue = 950000
    print(revenue)
    for letter in string1:
        sleep(0.0035) 
        sys.stdout.write(letter)
        sys.stdout.flush()
    for letter in string3:
        sleep(0.02) 
        sys.stdout.write(letter)
        sys.stdout.flush()
    

elif answer1 == C:
    revenue = revenue * 1.05
    

# sleep(0.5)
# print("------------------------------------------------------------")
# print("Financial Projections:     |       Stakeholder Satisfaction:")
# print("------------------------------------------------------------")
# print("Revenue: €1,000,000        |    Shareholders:         😐    ")
# print("Expenses:  €700,000        |    Customers:            😐    ")
# print("Profits:   €300,000        |    Employees:            😐    ")

