#Programmer: RaVon Rhone
#Date:10/7/2017
#if 1 year = 1.6 millimeters
#then 0.5 year = ?
print("Year\t", "Sea level Rise\n------\t------")

seaLevelRise = 0

for currentYear in range(1,26):
    seaLevelRise = currentYear * 1.6
    print( currentYear, "\t", format( seaLevelRise, ".2f" ))
