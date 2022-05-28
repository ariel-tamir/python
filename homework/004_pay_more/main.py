hours = input("Enter Hours: ")

try:
    hours = float(hours)
except:
    print("Error, please enter numeric input")
    exit()

rate = input("Enter Rate: ")

try:
    rate = float(rate)

except:
    print("Error, please enter numeric input")
    exit()

if hours > 40:
    pay_40 = 40 * rate + ((hours - 40) * rate * 1.5)
    print("Pay: {}".format(pay_40))

else:
    pay = hours * rate
    print("Pay: {}".format(pay))
