def while_loop(num):
    i = 0
    numbers = []

    while i < num:
        print(f"at the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("numbers now:", numbers)
        print(f"at the bottom i is {i}")


while_loop(6)
print("the numbers: ")

