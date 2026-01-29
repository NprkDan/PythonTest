for num in range(1, 51):
    if num < 2:
        print(f"{num} is NOT a prime number.")
    else:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
 
        if is_prime:
            print(f"{num} is a PRIME number.")
        else:
            print(f"{num} is NOT a prime number.")
 
 