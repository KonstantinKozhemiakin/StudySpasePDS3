import random
from random_words import RandomWords
import time


def bubble_sort(data):
    length = len(data)
    for iIndex in range(length):
        swapped = False
        for jIndex in range(0, length - iIndex - 1):
            if data[jIndex] > data[jIndex + 1]:
                data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
                swapped = True
        if not swapped:
            break
    # return data


def selection_sort(data):
    for scanIndex in range(0, len(data)):
        minIndex = scanIndex
        for compIndex in range(scanIndex + 1, len(data)):
            if data[compIndex] < data[minIndex]:
                minIndex = compIndex
        if minIndex != scanIndex:
            data[scanIndex], data[minIndex] = data[minIndex], data[scanIndex]
    # return data


def insertion_sort(data):
    for scanIndex in range(1, len(data)):
        tmp = data[scanIndex]
        minIndex = scanIndex
        while minIndex > 0 and tmp < data[minIndex - 1]:
            data[minIndex] = data[minIndex - 1]
            minIndex -= 1
        data[minIndex] = tmp
    # return data


def partition(nums, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


def insertion_sort(nums):
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Insert the item
        nums[j + 1] = item_to_insert


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # We use the list lengths often, so it is handy to make variables
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # We check which value from the start of each list is smaller
            # If the item at the beginning of the left list is smaller, add it
            # to the sorted list
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # If the item at the beginning of the right list is smaller, add it
            # to the sorted list
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # If we've reached the end of the left list, add the elements
        # from the right list
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # If we've reached the end of the right list, add the elements
        # from the left list
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    # If the list is a single element, return it
    if len(nums) <= 1:
        return nums

    # Use floor division to get midpoint, indices must be integers
    mid = len(nums) // 2

    # Sort and merge each half
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Merge the sorted lists into a new one
    return merge(left_list, right_list)


def heapify(nums, heap_size, root_index):
    # Assume the index of the largest element is the root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index, and the element is greater
    # than the current largest element, then update the largest element
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # Do the same for the right child of the root
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # If the largest element is no longer the root element, swap them
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    # Create a Max Heap from the list
    # The 2nd argument of range means we stop at the element before -1 i.e.
    # the first element of the list.
    # The 3rd argument of range means we iterate backwards, reducing the count
    # of i by 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Move the root of the max heap to the end of
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


def generate_list(len_list, type_of_list, rand_start, rand_finish):
    if type_of_list == 'int':
        int_list = []
        for j in range(len_list):
            int_list.append(random.randint(rand_start, rand_finish))
        return int_list
    if type_of_list == 'float':
        float_list = []
        for j in range(len_list):
            float_list.append(random.uniform(rand_start, rand_finish))
        return float_list
    if type_of_list == 'words':
        str_list = []
        w = RandomWords()
        for j in range(len_list):
            str_list.append(w.random_word())
        return str_list


def measure(function, iteration, len_list, type_of_list, rand_start=0, rand_finish=1000):
    time_of_done = []
    for i in range(iteration):
        my_list = generate_list(len_list, type_of_list, rand_start, rand_finish)
        time_start = time.time()
        function(my_list)
        time_of_done.append(time.time() - time_start)
    return sum(time_of_done) / len(time_of_done)


my_sort_func = [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort]
test_iteration = 5
test_len = 500
print(f"Test iteration : {test_iteration}\nTest length: {test_len}")
print(r"int    float  words  type")
for i in range(0, len(my_sort_func)):
    print(
        f"{measure(my_sort_func[i], iteration=test_iteration, len_list=test_len, type_of_list='int', rand_start=0, rand_finish=1000):.4f} "
        f"{measure(my_sort_func[i], iteration=test_iteration, len_list=test_len, type_of_list='float', rand_start=0.1, rand_finish=100.0):.4f} "
        f"{measure(my_sort_func[i], iteration=test_iteration, len_list=test_len, type_of_list='words'):.4f} "
        f"{my_sort_func[i].__name__}: ")
