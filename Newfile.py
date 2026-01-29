def main():

    # We initialize choice to True so the loop starts
    active = True

    while active:
        print("\n Calculator Menu ---")
        try:
            option = int(
                input(
                    "Enter 1 to add, 2 to subtract, 3 to multiply, 4 to divide (or 0 to exit): "
                )
            )

            if option == 0:
                print("Exiting calculator...")
                active = False
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if option == 1:
                print(f"Result: {num1 + num2}")
            elif option == 2:
                print(f"Result: {num1 - num2}")
            elif option == 3:
                print(f"Result: {num1 * num2}")
            elif option == 4:
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Error: Cannot divide by zero!")
            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Error: Please enter numbers only!")


if __name__ == "__main__":
    main()
