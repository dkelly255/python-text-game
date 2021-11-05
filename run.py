# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from time import sleep
import sys

string = "Test of typewriter effect for use in text based python game\n"

for letter in string:
    sleep(0.04)
    sys.stdout.write(letter)
    sys.stdout.flush()

input("Press any key")
print("\n----------------------------------------------------------------------")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("|                                                                    |")
print("----------------------------------------------------------------------")