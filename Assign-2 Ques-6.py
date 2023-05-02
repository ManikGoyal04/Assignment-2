a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if a + b > c and b + c > a and c + a > b:
    print("Yes")
else:
    print("No")