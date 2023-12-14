num = int(input("Enter Your Number: "))

if num < 0:
    print("Factorial can't be Calculated for negative numbers !")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("The factorial of", num, "is", factorial)
