def string_to_decimal(input_string):
    result = 0

    length = len(input_string)

    for i, char in enumerate(input_string):
        char_value = ord(char) - (ord('a') - 1)
        
        power = length - i - 1
        
        result += char_value * (26 ** power)
    
    return result

def compare_strings(string1, string2):
    decimal_value1 = string_to_decimal(string1)
    decimal_value2 = string_to_decimal(string2)
    
    if decimal_value1 < decimal_value2:
        return f"'{string1}' is less than '{string2}'"
    elif decimal_value1 > decimal_value2:
        return f"'{string1}' is greater than '{string2}'"
    else:
        return f"'{string1}' is equal to '{string2}'"

string1 = "abc"
string2 = "defg"
comparison_result = compare_strings(string1, string2)
print(comparison_result)