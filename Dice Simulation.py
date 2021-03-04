#copyright HermanErKu 2021©
#Dice simulation
#Throws a dice and tells how many times you get 1 and 6 and how many times there are as many 1 as 6.

import random

varSame = 0 #variabel that counts how many times one and six has been the same

times = 1000 

for i in range(times): #Does the entire thing (times) times
  varOne = 0 #Variable that counts ones
  varSix = 0 #Variable that tells sixes
  
  for i in range(100): #Loops 100 times
    dice = random.randint(1,6) #Random number from 1 to 6
    print (dice) #Shows the random number
    if dice == 1: #If random number is 1
      varOne = varOne + 1 #Add a one in variable
    if dice == 6: #If random number is 6
      varSix = varSix + 1 #Add a six in variabel

  print ("Six =", varSeks) #Tells you how many ones you got in "Six="
  print ("One =", varEn) #Tells you how many ones you got in "One="

  if varOne == varSix: #If how many times you got one = how many times you got six
    varSame = varSame + 1 #Add one in same variable

print ("One and six was the same", varSame,"out of", times, "times") #Tells you how many times they were the same
