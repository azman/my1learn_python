# howto: print text
# howto: get input from user
# howto: display variable

print("This is "+"awesome!")
# this is for 2.7 - in v>3.4, input acts like raw_input
# - in 2.7, input function WILL format the input accordingly
name = raw_input("Please enter your name: ")
print("Hello, " + name + "!")
year = raw_input("Please enter the year you were born: ")
print("You were born in year " + year + "?" )
age1 = 2019-int(year)
print("That means you are " + str(age1) + " years old!")
