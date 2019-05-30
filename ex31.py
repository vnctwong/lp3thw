print(
    """you enter dark room w/ 2 doors.
#1 or 2"""
)

door = input(">")

if door == "1":
    print("there is bear")
    print("what do")
    print("1. cake")
    print("2. scream")

    bear = input(">")

    if bear == "1":
        print("bear eats")
    elif bear == "2":
        print("bear eats 2")
    else:
        print(f"well doing {bear} is probs better")
        print("bear runs away")

        insanity = input(">")

        if insanity == "1" or insanity == "2":
            print("you survive")
            print("gj")
        else:
            print("rots")
            print("gj")

else:
    print("fall on knife")

