import random
num=100
rand=random.randrange(1,num)

print("Guess the number between 1 to 100")
while True:
  guess=int(input("Guess the number"))
  
  if guess>num:
    print("the number is invalid,enter the number between 1 to 100")
    break
  
  if rand==guess:
    print("your guess is correct")
    break
  elif rand>guess:
    print("your enter number is lessthan the guesser number")
  elif rand<guess:
    print("your enter number is greater the guess number") 
  else:
    pass