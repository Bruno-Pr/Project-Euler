min_num : int = 0
i : int = 0
i2 : int = 0
not_divisable : bool = True

while not_divisable :
    if i % 7 == 0 and i % 11 == 0 and i % 13 == 0 and i % 17 == 0 and i % 19 == 0  and i % 20 == 0:
        for i2 in range(1, 20) :
            if i % i2 == 0 :
                print(f"Atual número sendo testado: {i}")
                if i2 == 20 :
                    min_num = i
                    not_divisable = False

                else:
                    continue

            else:
                continue

    i += 1

print(f"Mínimo multiplo comum de 1 á 20: {min_num}")