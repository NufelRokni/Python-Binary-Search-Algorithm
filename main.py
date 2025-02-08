from binary_search import binarySearch

if __name__ == "__main__":
    # Example usage
    ordered_array = [1, 3, 5, 7, 9, 11, 32, 43, 64, 73, 87, 96, 102]
    target_value = 7
    result = binarySearch(ordered_array, target_value)
    
    if result != -1:
        print(f"Element {target_value} found at index {result}")
    else:
        print(f"Element {target_value} not found")
