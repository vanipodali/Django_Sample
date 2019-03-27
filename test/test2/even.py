def print_even_odd(limit):
    number_dict = {}
    for each in range(0, limit):
        if each % 2 == 0:
            if 2 in number_dict:
                number_dict[2].append(each)
                if each % 2 != 0:
                    number_dict[2].append(each)
    return number_dict
print(print_even_odd(1000))
