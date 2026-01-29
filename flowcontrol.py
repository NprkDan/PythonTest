# for loop control

num = int(input("Enter a number:"))
# print(num +   1  ) # type: ignore

for i in range(1, 12):
    print(num, " * ", i, " = ", num * i)
# ----------------------------------------
age = int(input("Enter the age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
# ----------------------------------------
number_to_check = int(input("Enter a number to check Prime or not: "))
is_prime = True
for i in range(2, number_to_check):
    if number_to_check % i == 0:
        is_prime = False
        break
if is_prime:
    print(number_to_check, "is a Prime number")
else:
    print(number_to_check, "is not a Prime number")
# ----------------------------------------
# A script to check numbers from 1 to 50 and identify if they are prime.


def is_prime(n):

    if n < 2:
        return False
    # We check divisors up to the square root of n for efficiency
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# check it the numbers from 1-50 are prime or not)


def main():

    print("--- Prime Number check (1-50) ---")

    for num in range(1, 51):
        if 1 % i == 0:
            print(f"{num} is a PRIME number.")
        else:
            print(f"{num} is NOT prime.")


if __name__ == "__main__":
    main()
