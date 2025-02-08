def binarySearch(array, target_value):
    left_pointer, right_pointer  = 0, len(array) - 1
    
    while(left_pointer <= right_pointer):
        middle_pointer = (left_pointer + right_pointer) // 2
        if array[left_pointer] == target_value: return left_pointer
        if array[right_pointer] == target_value: return right_pointer
        if array[middle_pointer] < target_value: left_pointer = middle_pointer
        else: right_pointer = middle_pointer
        
    return -1


if __name__ == '__main__':
    # Example usage
    ordered_array = [1, 3, 5, 7, 9, 11, 32, 43, 64, 73, 87, 96, 102]
    target_value = 7
    result = binarySearch(ordered_array, target_value)
    print("Target found at index:", result)