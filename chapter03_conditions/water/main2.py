water = input("amount of water glasses: ")
try:
    water = int(water)
except:
    print("please enter an integer")
    exit()

if water >= 8:
    print("Well done")
elif 4 <= water <= 7:
    print("You can do better")
else:
    print("OMG!! go to drink now!")
