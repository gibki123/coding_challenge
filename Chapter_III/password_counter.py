counter = 0
previous_char = None
double_word_counter = 0
is_valid = True
current_digit_group = None

for i in range(372**2, 809**2 + 1):
    string_int = str(i)
    for char in string_int:
        if previous_char is not None:
            if char == previous_char:
                if char != current_digit_group:
                    current_digit_group = char
                    double_word_counter += 1
            else:
                current_digit_group = None
                if previous_char > char:
                    is_valid = False
                    break
        previous_char = char
    if double_word_counter < 2:
        is_valid = False
    if is_valid is True:
        counter += 1
    previous_char = None
    double_word_counter = 0
    is_valid = True

print(counter)
