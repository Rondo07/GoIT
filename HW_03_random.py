import random


def get_numbers_ticket(min, max, quantity):   # Define function
    if min < 1 or max > 1000 or min > max:   # Check the condition for min and max
        return []
    range_numbers = max - min + 1
    if quantity > range_numbers:   # Check the condition for quantity > min-max range
        return []
    
    lottery_numbers = set()   # Create an empty set
    while len(lottery_numbers) < quantity:   # Generate numbers in a while-loop
        lottery_numbers.add(random.randint(min, max))   # Use random.randint to get numbers
    return sorted(lottery_numbers)


lottery_numbers = get_numbers_ticket(1, 100, 4)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(10, 14, 6)
print("Ваші лотерейні числа:", lottery_numbers)
