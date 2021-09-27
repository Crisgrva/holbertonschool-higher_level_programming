#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    tmp_result = 0
    result = []
    for num in range(0, list_length):
        try:
            tmp_result = my_list_1[num] / my_list_2[num]
        except (ZeroDivisionError, TypeError, IndexError):
            tmp_result = 0
        finally:
            result.append(tmp_result)
    return result
