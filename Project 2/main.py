import random
import time

# Record the start time
start_time = time.time()


# Function to divide the array into 3 parts according to the pivot element
def divide_array(array1, pivot):
    left = [x for x in array1 if x < pivot]
    right = [x for x in array1 if x > pivot]
    equal = [x for x in array1 if x == pivot]
    return left, equal, right


def quick_select(array2, k):
    # If the array size is small, i.e less than 5, sort it and return the k-th element
    if len(array2) < 5:
        array2.sort()
        return array2[k]

    # Else, if array is large, then Split the array into groups of 5 elements each
    groups = [array2[i:i+5] for i in range(0, len(array2), 5)]

    # Calculate the medians of each group
    medians = [sorted(group)[len(group) // 2] for group in groups]

    # Find the median of medians using recursion
    median_of_medians = quick_select(medians, len(medians) // 2)

    # divide the array into three parts: <pivot, =pivot, >pivot
    left, equal, right = divide_array(array2, median_of_medians)

    if k < len(left):
        return quick_select(left, k)
    elif k < len(left) + len(equal):
        # If k is within the equal group, return the median_of_medians
        return median_of_medians
    else:
        # Recursively search in the right group with adjusted k
        return quick_select(right, k - len(left) - len(equal))


# As we need to analyse the time complexity for different input size, we generate random numbers and insert in array
array0 = []
def array_build(inp_size):
    for i in range(0, inp_size):
        array0.append(random.randint(99, 500))


# We specify the input size here
input_size = 10000000
array_build(input_size)
k = 5000000  # Find the kth smallest element
result = quick_select(array0, k-1)


# Record the end time
end_time = time.time()


# Calculate the execution time in milliseconds
execution_time_ms = (end_time - start_time) * 1000


print(f"The {k}-th smallest element is: {result}")
print(f"Execution time: {execution_time_ms:.2f} milliseconds")