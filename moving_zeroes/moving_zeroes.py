'''
Input: a List of integers
Returns: a List of integers

Write a function that takes an array of integers and moves each non-zero integer to the left side of the array, then returns the altered array. The order of the non-zero integers does not matter in the mutated array.

Notes:
- takes in an array of ints
- moves non-zeros int to the left
- returns array 

- loop through list
- if there's a 0 in the list
    - remove it - then append to the end
'''


def moving_zeroes(arr):
    # Your code here

    for i in arr:
        if i == 0:
            arr.remove(i)
            arr.append(i)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
