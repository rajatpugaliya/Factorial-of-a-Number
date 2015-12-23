num = input("Enter a number: ") # take input from the user
factorial = 1
if num < 0: # check if the number is negative or not
   print("factorial is not possible for negative no.")
elif num == 0: # check if the number is 0
   print("The factorial of 0 is 1")
else:
   for i in range(1,num+1):
       factorial = factorial*i
   print "The factorial of",num,"is",factorial