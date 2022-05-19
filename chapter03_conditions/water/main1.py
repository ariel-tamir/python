water = input("amount of water glasses: ")
water = int(water)
if water >= 8:
    print("Well done")
else:
    if water >= 4 and water <= 7:
        print("You can do better")
    else:
        print("OMG!! go to drink now!")
