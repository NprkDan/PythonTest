option = int(input("Enter 1 to add, 2 to subtract, 3 to multiply, 4 to divide, 0 to exit: "))
 
    if option == num1:
        break
    elif option in (1, 2, 3, 4):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
 
        if option == 1:
            print(num1 + num2)
        elif option == 2:
            print(num1 - num2)
        elif option == 3:
            print(num1 * num2)
        elif option == 4:
            if num2 != 0:
                print(num1 / num2)
            else:
                print("Error: Cannot divide by 0")
    else:
        print("Invalid option.")