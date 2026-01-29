try:
    result = 10 / 0
    print("Results is:", result)
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.", e)
except Exception as e:
    print("An unexpected error occured:", e)
finally:
    print("execuition completed.")
