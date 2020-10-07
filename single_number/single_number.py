'''
Given a non-empty array of integers where every element appears twice except for one. Find that single number. You may assume that there will _always_ be _one_ odd-number-out and every other number in the input shows up exactly twice.

Input: a List of integers where every int except one shows up twice
Returns: an integer
- loop through the array of integers 
  - check if there's a double number
    - if so, break
    - if find single number, return that number
'''
from iteration_utilities import duplicates


def single_number(arr):
    # Your code here
    single = set()
    for i in arr:
        if i in single:
            j = list(single)
            res = str(j)[1:-1]
            return res
        else:
            single.add(i)


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
