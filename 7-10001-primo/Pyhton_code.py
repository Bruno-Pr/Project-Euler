current_num : int = 1
primes_list : list = []
i : int = 0
i2 : int = 0

while i <= 10001 :
    for i2 in range(2, current_num) :
        if current_num % i2 == 0 :
            break

        elif i2 == current_num - 1 :
            primes_list.append(current_num)
            i += 1

    current_num += 1

print(f"10,001 número primo: {primes_list}")
print(f"10,001 número primo: {primes_list[10000]}")