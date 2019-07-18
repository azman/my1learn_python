# howto: detect input error (using exception)

print("This is "+"awesome!")
# this is for 2.7 - in v>3.4, input acts like raw_input
name = raw_input("Please enter your name: ")
print("Hello, " + name + "!")
year = raw_input("Please enter the year you were born: ")
try :
  test = int(year)
  print("You were born in year " + year + "?" )
  age1 = 2019 - test
  print("That means you are " + str(age1) + " years old!")
except ValueError :
  print("Is '" + year + "' a valid year?")
