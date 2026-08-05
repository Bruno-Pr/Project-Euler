range_limit : int = 4000000
even_fibonacci_num_list : list = [2]

i : int = 0
last_num : int = 1
current_num : int = 2


while i < range_limit :
    i = current_num + last_num

    if i % 2 == 0 :
        even_fibonacci_num_list.append(i)

    last_num = current_num
    current_num = i

print(f"Números de Fibonacci pares abaixo de 4,000,000: {even_fibonacci_num_list}")

num_soma : int = sum(even_fibonacci_num_list)
print(f"Soma dos números pares de Fibonacci abaixo de 4,000,000: {num_soma}")
