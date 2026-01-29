# __ask age in numbers error on letters


def get_int_from_user(prompt):
    while True:
        try:
            val = int(input(prompt))
            return val  # if value not correct
        except ValueError:
            print("That's not the number")


age = get_int_from_user("Your age?: ")
print("please continue")
