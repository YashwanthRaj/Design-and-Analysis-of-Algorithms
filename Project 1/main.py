import time

# Record the start time
start_time = time.time_ns()

def partition(arr, pivot):
    # Partition the array into elements <= pivot and elements > pivot
    left = [x for x in arr if x <= pivot]
    right = [x for x in arr if x > pivot]
    return left, right


def quick_select(arr, k):
    if len(arr) < 5:
        # If the array size is small, sort it and return the k-th element
        arr.sort()
        return arr[k]

    # Split the array into chunks of 5 elements
    chunks = [arr[i:i + 5] for i in range(0, len(arr), 5)]

    # Calculate the median of each chunk
    medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]

    # Find the median of medians
    median_of_medians = quick_select(medians, len(medians) // 2)

    # Partition the array into L and R based on the median_of_medians
    L, R = partition(arr, median_of_medians)

    if k < len(L):
        # k-th element is in L
        return quick_select(L, k)
    elif k >= len(arr) - len(R):
        # k-th element is in R
        return quick_select(R, k - (len(arr) - len(R)))
    else:
        # k-th element is the pivot
        return median_of_medians


# Example usage
arr = [3, 1, 8, 4, 7, 5, 6, 2]
k = 3  # Find the 3rd smallest element
result = quick_select(arr, k - 1)  # Subtract 1 from k for 0-based indexing
print(f"The {k}-th smallest element is: {result}")

# Record the end time
end_time = time.time_ns()

# Calculate the elapsed time in nanoseconds
elapsed_time_ns = end_time - start_time
print(f"Elapsed Time: {elapsed_time_ns} nanoseconds")