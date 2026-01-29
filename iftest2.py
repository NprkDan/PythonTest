print("--- Prime numbers from 1 to 20 ---")
 
for num in range(1, 21):
    if num > 1:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
 
        if count == 2:
            print(num)