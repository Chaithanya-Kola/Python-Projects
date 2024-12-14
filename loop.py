number_1 = int(input("Enter a first number: "))
number_2 = int(input("Enter a second number: "))
for i in range(number_1, number_2):
    if i >= number_1 and i <= number_2:
        print(i)
    else:
        print("Number is out of range")