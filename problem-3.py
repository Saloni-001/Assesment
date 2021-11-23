a = int(input("Enter a number: "))
if a % 2 == 0:
    a = a - 1
for i in range(a):
    print(i + (i + 1), end=" ")
    i += 1
