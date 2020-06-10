'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    new_arr = list(arr)
    for i in range(len(arr)):
        item = new_arr.pop(i)
        total = 1
        for j in new_arr:
            total *= j
        arr[i] = total
        new_arr.insert(i, item)
        total = 1
    return arr
if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [1, 7, 3, 4]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
