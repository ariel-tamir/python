text = input("Enter the string: ")
location = input("Enter the location: ")
times = input("Enter the times: ")
location = int(location)
tail = text[location:]
times = int(times)
many = tail * times

print("The result is: {}".format(many))
