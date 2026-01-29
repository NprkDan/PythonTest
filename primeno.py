def prime():
    print("check if numbers 1-50 for prime number")


for num in range(1, 50):
    if is_prime(num):
        print(f"{num} is prime no.")
    else:
        print(f"{num} is not prime no.") 
        
