def print_only_odd_numbers_in_a_list(number_list):
    for number in number_list:
        if number % 2 != 0:
            print(number)
        
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_only_odd_numbers_in_a_list(numbers)