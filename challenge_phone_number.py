"""
Implement a function that accepts an array of 10 integers. Have the function return those numbers as a String in
the form of a phone number. Please use the following format for the phone number: (XXX) XXX-XXXX. Integers in the
array will be no larger than 9.
"""


def create_phone_number_my_solution(arr):
    phone_number = "("
    for num in arr:
        phone_number = phone_number + str(num)
        if len(phone_number) == 4:
            phone_number = phone_number + ") "
        if len(phone_number) == 9:
            phone_number = phone_number + "-"

    return phone_number


def create_phone_number_top_solution(arr):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*arr)


print(create_phone_number_my_solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number_my_solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

print(create_phone_number_top_solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number_top_solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
