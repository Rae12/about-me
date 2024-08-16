#Programmer: RaVon Rhone
#Date: 10/7/2017
#Write a program that calculates the number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, with the minimum amount of leftovers.

hotDogsInAPackage = 10
hotDogBunsInAPackage = 8

numberOfPeople = int(input("Please enter the number of people " +\
                           "attending the cookout:"))

hotDogsEach = int(input("Please enter the number of hot dogs each " +\
                        " of the " + str(numberOfPeople)+\
                        " people is going to get: "))

hotDogsNeeded = numberOfPeople * hotDogsEach
hotDogBunsNeeded = hotDogsNeeded

exactHotDogPackages = hotDogsNeeded / hotDogsInAPackage
exactHotDogBunsPackages= hotDogBunsNeeded / hotDogBunsInAPackage

hotDogPackagesRemainder = hotDogsNeeded % hotDogsInAPackage
hotDogBunsRemainder = hotDogBunsNeeded % hotDogBunsInAPackage

if hotDogPackagesRemainder > 0:
    minimumHotDogPackagesRequired = int(exactHotDogPackages + 1)
else:
    minimumHotDogPackagesRequired = int(exactHotDogPackages)


if hotDogBunsRemainder > 0:
    minimumHotDogBunPackagesRequired = int(exactHotDogPackages + 1)
else:
    minimumHotDogBunPackagesRequired = int(exactHotDogBunsPackages)

hotDogsLeftOver = int(float(format(minimumHotDogPackagesRequired - \
                         exactHotDogPackages, ".2f")) * hotDogsInAPackage)
hotDogBunsLeftOver = int(float(format(minimumHotDogPackagesRequired - \
                            exactHotDogBunsPackages, ".2f")) * hotDogsInAPackage)

print("\nMinimum number of packages of hot dogs required: " +\
      str(minimumHotDogPackagesRequired) + "\nMinimum number of packages " \
      "of hot dogs buns required: " + str(minimumHotDogBunPackagesRequired)\
      +"\nHot dogs left over: " + str(hotDogsLeftOver) + "\nThe number"\
      "of hot dog buns that will be left over: " + str(hotDogBunsLeftOver))



