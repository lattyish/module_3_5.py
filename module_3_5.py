def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) <= 1:
        return int(str_number)

    first = int(str_number[0])
    remaining_number = int(str_number[1:])
    if remaining_number == 0:
        return first
     return first * get_multiplied_digits(remaining_number)
result = get_multiplied_digits(304000)
print(result)
