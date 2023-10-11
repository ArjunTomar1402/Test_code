def conversion(input_str):
    result = 0
    length = len(input_str)
    for i,char in enumerate (input_str):

        char_value = ord(char) - (ord('a') -1)
        power = length -i - 1
        result += char_value * (26 ** power)

    return result

input_str = 'abcbb'
decimal_value = conversion(input_str)
print("The decimal value of is",decimal_value) 
# print("The decimal value of is",char_value) 