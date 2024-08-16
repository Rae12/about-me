#Programmer:RaVon Rhone
#Date:10-7-2017
#Using While-Loop
#Reciprocals
#prints the reciprocals of 2 to 10.

denominator = 2
while denominator <= 10:
    print ("1/" + str(denominator), "=",(1.0/denominator))
    denominator = denominator + 1


#Using For-Loop

for i in range(2,11):
    print("1/" + str(i) + " is " + str(1.0/i))
