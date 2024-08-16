#Programmer:RaVon Rhone
#Date:10/7/2017
#Write a program, using fuctions, to print the lyrics of the sone " Old MacDonald". Your program shoudl print the lyrics for five different animals, similar to the example vers below:#
# define a "farmer" function that gets two parameters: "animal" and "noise"
#     print out the lyrics to the song, substituting in the animal and noise where appropriate

# define a "main" function
#     call the farmer function with parameters "cow" and "moo"
#     call the farmer function with parameters "pig" and "oink"
#     etc.
#     (Consider calling the farmer function from a loop?)

# if __name__ == "__main__":
#     main()


def farmer(animal, noise):
    print("Old MacDonald had a far, Ee-igh, Ee-igh, Oh!")
    print("And on that farm he has a", animal, ", Ee-igh, Ee-igh, Oh!")
    print("With a", noise, noise,"here, and a ", noise, noise, noise," there.")
    print("Here a", noise, ", there a", noise, ", everywhere a", noise, noise,".")
    print("Old MacDonald has a farm, Ee-igh, Ei-igh, Oh!")
    print()

def main():
    farmer("cow","moo")
    farmer("chicken","cluck")
    farmer("sheep","baa")
    farmer("horse","neigh")
    farmer("pig","onik")

if __name__ == "__main__":
    main()













































