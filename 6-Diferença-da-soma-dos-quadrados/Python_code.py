desired_range : int = 100

sum_of_num : int = 0
squared_num : int = 0
squared_sum : int = 0
sum_of_squares : int = 0
sum_square_difference : int = 0

i : int = 0

for i in range(desired_range) :
    sum_of_num += i
    squared_num = pow(i, 2)
    sum_of_squares += squared_num

squared_sum = pow(sum_of_num, 2)
sum_square_difference = squared_sum - sum_of_squares

print(f"Diferença da soma dos quadrados: {sum_square_difference}")