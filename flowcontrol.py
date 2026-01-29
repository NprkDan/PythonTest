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






