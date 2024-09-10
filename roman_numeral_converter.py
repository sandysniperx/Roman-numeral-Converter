def roman_to_number(roman):
    
    roman_numerals = {    'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    
    total = 0
    prev_value = 0
    
    for char in reversed(roman.upper()):
        value = roman_numerals.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

def number_to_roman(num):

    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    
    roman = ''
    i = 0
    while num > 0:
        for _ in range(num // value[i]):
            roman += symbol[i]
            num -= value[i]
        i += 1
    
    return roman

print("[ Roman Numeral Converter ]")
print()
print("Choose the conversion type:")
print("[1 = Roman to Number] \n[2 = Number to Roman]\n")
print()
user_in = input("Enter 1 or 2: ")
print()

match user_in:
    case '1':  #rmn_to_num
        rmn_num = input("Enter a Roman numeral: ")
        if not all(char in 'IVXLCDM' for char in rmn_num):
            print("Invalid input.")
        else:
            num = roman_to_number(rmn_num)
            print(f"Number value: {num}")
        
    case '2':  #num_to_rmn
        num = input("Enter a number: ")
        if not num.isdigit():
            print("Invalid input.")
        elif int(num) <= 0:
            print("Roman numerals do not supported to handle 0 or negatives.")
        else:
            num_num = int(num)
            roman_value = number_to_roman(num_num)
            print(f"Roman numeral: {roman_value}")
        
    case _: 
        print("Invalid input.")