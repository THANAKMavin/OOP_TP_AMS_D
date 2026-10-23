width = 25
height = 6

for i in range(height):
    if i == 0 or i == height - 1:
        print("*" * width)

    else:
        print("*" + " " * (width - 2) + "*")
