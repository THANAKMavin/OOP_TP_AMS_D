n = 3
for i in range(n):
    if i == 0:
        print(" " * (n - 1) + "*")
    else:
        print(" " * (n - i - 1) + "*" + " " * (2 * i -1) + "*")

for i in range(n - 2, -1, -1):
    if i == 0:
        print(" " * (n - 1) + "*")
    else:
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")
