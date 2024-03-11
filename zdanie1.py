name = input("whats your name")

age = int(input("whats your age"))

nowyear = int(2024)

print("hello " + name)
print("your name has " + str(len(name)) + " letters and starts with " + name[0] )
print("now you have " , int(age) , "and in the next year you will have " , int(age)+1 , "year of birth is ", nowyear - age)