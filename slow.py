a = int(input("Enter a speed: "))
b = int(input("Enter another speed: "))
c = int(input("Enter another speed: "))
avg = (a + b + c)/3
if a<avg:
    print("a is slower than the average speed")
elif b<avg:
    print("b is slower than the average speed")
elif c<avg:
    print("c is slower than the average speed")
else:
    print("no one is slower than the average speed")