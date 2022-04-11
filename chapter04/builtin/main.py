no1 = input("number1: ")
no2 = input("number2: ")
no3 = input("number3: ")

no1 = int(no1)
no2 = int(no2)
no3 = int(no3)

highest = max(no1, no2, no3)
print("the highest is {}".format(highest))

lowest = min(no1, no2, no3)
print("the lowest is {}".format(lowest))
