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


string = "- The Year is 2021...\n- FictionalCorp have hired you as their new CEO\
\n- You have been tasked with improving their performance on three fronts\
    \nin the coming financial year\
    \n- You will receive one point for each improvement in stakeholder sentiment\
    \n- You will lose one point for each decline in stakeholder sentiment\
    \n- Navigate the following series of business decisions, and their respective\
    \nstakeholder impacts\n" 

for letter in string:
  sleep(0.02) # In seconds
  sys.stdout.write(letter)
  sys.stdout.flush()

input("\n[Press Enter To Begin]")