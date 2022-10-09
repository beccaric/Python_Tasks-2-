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

#Challenge 3 - using logic operators (and)
age=int(input("How old are you?: "))
BritishCitizen=input("Are you a British citizen?: ")
if age>=18 and BritishCitizen == "Yes":
  print("You are able to vote!")
else:
  print("You are either too young or you are not a British Citizen")


#Challenge 4 - using logic operators (or)
number=int(input("Enter a number less than 6:"))
if number == 1 or number ==3 or number ==5:
  print("You have entered an odd number!")
else:
  print("You have entered an even number!")

#Challenge 5 - using boolean variables and NOT operator
ShoePrice = float(input("Enter a price: "))

if(ShoePrice <9.99):
  cheapShoe= True
else:
  cheapShoe= False

if(not(cheapShoe)):
  print("The shoe is expensive")
else: 
  print("The shoe is cheap")


#For LOOP
for number in range (1,6):
  print(number)

for number in range (2,48,2):
  print(number)

#while LOOP
again = "yes"
while again == "yes":
  print("hello")
  again=input("Do you want to loop again?")
  