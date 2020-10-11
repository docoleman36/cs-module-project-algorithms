# Single Number

Given a non-empty array of integers where every element appears twice except for one. Find that single number. You may assume that there will _always_ be _one_ odd-number-out and every other number in the input shows up exactly twice.

## Examples

```
Sample input: [2, 2, 1]
Expected output: 1
```

```
Sample iput: [4, 1, 2, 1, 2]
Expected output: 4
```

Can you implement a solution that finds the single number in _one_ pass through the input array with `O(1)` space complexity?

## Testing

Run the test file by executing `python test_single_number.py`.

## Notes

- Array is non-empty
- Find single number integer
- Is there more than 1 number that is a single number?

### Ways to solve

- loop through the array of integers
  - check if there's a double number
    - if so, break
    - if find single number, return that number
