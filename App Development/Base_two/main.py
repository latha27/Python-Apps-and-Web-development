import math


# user_input = input("Enter the array:")
A = [1, 0, 0, 1, 1, 1]
int_range = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
special_characters = "!@#$%^&*()-+?_=,<>/"


def generate_base_bit(n_int):
    base_num_generator = []
    length = list(range(len(n_int)))
    for i in length:
        num = (pow(-2, i))
        base_num_generator.append(num)
    return base_num_generator


def int_to_base_generator(array_a):
    try:
        base_to_int = 0
        int_generate = generate_base_bit(int_range)
        length_a = list(range(len(array_a)))
        for i in length_a:
            number = array_a[i] * int_generate[i]
            base_to_int = base_to_int + number
        int_to_int_convertor = math.ceil(base_to_int / 2)
        s = ""
        while int_to_int_convertor != 0:
            if int_to_int_convertor % 2 == 0:
                s = "0" + s
            else:
                s = "1" + s
                int_to_int_convertor = int_to_int_convertor - 1
            int_to_int_convertor = int_to_int_convertor / -2
        if s == "":
            s = "0"
        reverse_string = s[::-1]
        actual_output = []
        for i in reverse_string:
            actual_output.append(int(i))
        return actual_output
    except TypeError:
        return "Allowed only binary numbers(0, 1). Please enter correct input"


print(int_to_base_generator(A))



