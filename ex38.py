ten_things = "apple orang crow tele"

print("list not enough things")

stuff = ten_things.split(" ")
more_stuff = ["dat", "day", "yay", "ay"]

while len(stuff) != 8:
    next_one = more_stuff.pop()
    print("adding: ", next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now.")

print("there we go: ", stuff)

print("lets do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(" ".join(stuff))
print("#".join(stuff[3:5]))

