'''
Write a function that receives an array of integers and returns an array consisting of the product of all numbers in the array except the number at that index.

Input: a List of integers
Returns: a List of integers

Notes:
- loop through all the numbers 
- multiple each number in the array except for that index

step:
- multiply each number in an array
- after after multiply everything except for current index
'''


def product_of_all_other_numbers(arr):
    prod = 1

    for i in arr:
        prod *= i

    all_nums = [prod//i for i in arr]
    return all_nums


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
