pasta = input("do you like pasta? ")
pasta = (pasta == 'true')

broccoli = input("do you like broccoli? ")
broccoli = (broccoli == 'true')

if pasta and broccoli:
    print("Yucky")
elif pasta:
    print("Yammy")
elif broccoli:
    print("Yammy")
else:
    print("hungry")
