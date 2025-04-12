a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if a % b == 0:
    print(a, " is divisible by ", b)
elif b % a == 0:
    print(b, " is divisible by ", a)
else:
    print(a, " is not divisible by ", b, " and ", b, " is not divisible by ", a)