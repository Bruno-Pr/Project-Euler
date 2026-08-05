largest_palindrome : int = 0
product_num : int = 0
num_string : str = ""
reversed_num : str = ""
i : int = 0
i2 :int = 0

for i in range(999) :
    for i2 in range(999) :
        product_num = i * i2
        num_string = str(product_num)
        reversed_num = num_string[::-1]
        if reversed_num == num_string and product_num > largest_palindrome :
            largest_palindrome = product_num
            #print(f"Maior número palindromico atual: {largest_palindrome}")
            

print(f"Maior número palindromico: {largest_palindrome}")