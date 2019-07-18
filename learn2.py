# howto: branch statement (selection)

mark = raw_input("Enter your mark: ")
mark = int(mark)

if mark > 100 or mark < 0 :
  print("That is out of valid range!")
elif mark >= 80 :
  print("Grade : A")
elif mark >= 75 :
  print("Grade : A-")
elif mark >= 70 :
  print("Grade : B+")
elif mark >= 65 :
  print("Grade : B")
elif mark >= 60 :
  print("Grade : B-")
elif mark >= 55 :
  print("Grade : C+")
elif mark >= 50 :
  print("Grade : C")
elif mark >= 45 :
  print("Grade : C-")
elif mark >= 40 :
  print("Grade : D+")
elif mark >= 35 :
  print("Grade : D")
elif mark >= 30 :
  print("Grade : D-")
else:
  print("Grade : F")
