array = [3, 4, 5, 6, 2, 1]


def linear_search(array, val):
    for array_val in array:
        if array_val == val:
            return True
    return False


    # or using the position

def linear_search(array, val):
    for position in range(len(array)):
        if array[position] == val:
            return True
    return False

    # recursive

def linear_search(array, val, position):
    if array[position] != val:
        return linear_search(array, val, position+1)
    else: 
        return True

# Binary search recursive

def binary_search(array, val):
    left, right = 0, len(array)-1
    if left <= right:
        middle = (right + left) // 2
        if array[middle] == val:
            return True
        
        if array[middle] > val:
            return binary_search(array[:middle], val)
        elif array[middle] < val:
            return binary_search(array[middle+1:], val)
    
    return False

binary_search(sorted(array), 4)


# selection sort O(nˆ2)

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(min_index + 1, len(array)): # if you use range() you can put len(array) instead of len(array)-1
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

selection_sort(array)

# bouble sort O(nˆ2)

def bouble_sort(array):
    for j in range(len(array)):
        for i in range(len(array)):
            if i < len(array)-1:
                if array[i] > array[i+1]:
                    array[i], array[i+1] = array[i+1], array[i]
    return array
        
bouble_sort(array)


# merge sort n(n log n)

def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i] < left[j]:
               array[k] = left[i]
               i+=1
            else:
                array[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            array[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            array[k]=right[j]
            j=j+1
            k=k+1

