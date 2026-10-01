def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()

    return unique_numbers[-2]