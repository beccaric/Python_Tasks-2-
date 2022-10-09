#Python tasks - 04 October 

#Challenge 1
name=input("Please enter your name: ")
FirstNumber=int(input("Please enter a number: "))
SecondNumber=int(input("Please enter a second number: "))
if FirstNumber >SecondNumber:
  print (SecondNumber, FirstNumber)
else:
  print(FirstNumber, SecondNumber)

  
#Challenge 2
number=input("Please enter 1, 2, or 3: ")
if number == "1":
  print("Thank you!")
elif number == "2":
  print ("Well done!")
elif number == "3":
  print ("Correct!")
else:
  print ("Error")
