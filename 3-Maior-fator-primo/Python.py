target_number : int = 600851475143
biggest_prime_factor : int = 0
i : int = 0
i2 : int = 0


for i in range(1, target_number) :
    if target_number % i == 0 :
        prime_check : int = i
        not_prime : bool = False
        for i2 in range(2, (prime_check // 2)) :
            if prime_check % i != 0 :
                not_prime = True
                break

        if not_prime :
            continue

        if i > biggest_prime_factor :
            biggest_prime_factor : int = i

print(f"Maior fator primo: {biggest_prime_factor}")
