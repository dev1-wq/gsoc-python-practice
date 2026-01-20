# Find the largest element in a list.

elements = input("Enter numbers separated by space: ")


numbers = elements.split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])


def find_largest(nums):
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    return largest

print("Largest element is:", find_largest(numbers))
