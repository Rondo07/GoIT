import re

def normalize_phone(phone_number):   # Create a function
    sanitized_number = re.sub(r'[^\d+]',  '', phone_number)   # Remove all non-digit characters except +
    if sanitized_number.startswith('+'):   # Check if number starts with +
        return sanitized_number
    if sanitized_number.startswith('380'):   # Check if number starts with 380
        sanitized_number =  '+' + sanitized_number   # Add + to number
    else:
        sanitized_number = '+38' + sanitized_number   #Otherwise add +38 to number
    return sanitized_number

raw_numbers = [
    "+44 7911123456",
    "+49 151-234-567-89",
    "+33 612 3456 78",
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]   # Normalize all numbers and create a list
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
