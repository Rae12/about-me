#Programmer:RaVon Rhone
#Date: 10/7/2017
#Write a program that outputs all the odd integers less than 50 on one line,
#as well as the sum of those odd integers at the end on the next line
n = 50
i = 1
total = 0
while i < n:
    print (i, end=' ')
    total += i 
    i += 2
print()
print("Total = ",total)
    
