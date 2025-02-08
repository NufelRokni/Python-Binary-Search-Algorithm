def binarySearch(arrary, target_value):
    if len(arrary) == 0: 
        return -1
    
    left_pointer, right_pointer  = 0, len(arrary) - 1
    
    if arrary[left_pointer] > target_value or arrary[right_pointer] < target_value: 
        return -1
    
    while(left_pointer <= right_pointer):
        middle_pointer = (left_pointer + right_pointer) // 2
        if arrary[middle_pointer] == target_value: 
            return middle_pointer
        elif arrary[middle_pointer] < target_value: 
            left_pointer = middle_pointer + 1
        else: 
            right_pointer = middle_pointer - 1
        
    return -1