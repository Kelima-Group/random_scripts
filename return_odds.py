def return_odd_numbers(numbers):

    return [num for num in numbers if num % 2 != 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(return_odd_numbers(numbers))
