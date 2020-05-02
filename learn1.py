# howto: print text
# howto: get input from user
# howto: display variable

from datetime import date
import sys

def get_input(ask):
  if sys.version_info[0] < 3 or sys.version_info[1] < 4:
    temp = raw_input(ask)
  else:
    temp = input(ask)
  return temp

def get_year():
  year = date.today().strftime("%Y")
  return int(year)

print("This is "+"awesome!")
name = get_input("Please enter your name: ")
print("Hello, " + name + "!")
year = get_input("Please enter the year you were born: ")
print("You were born in year " + year + "?" )
age1 = get_year()-int(year)
print("That means you are " + str(age1) + " years old!")
