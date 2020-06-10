'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    running = True
    i=0
    count = 1
    while running:
        if arr[i] == 0:
            arr.append(arr.pop(i))
            count += 1
            i-=1
        i+=1
        if i >= len(arr)-count:
            running = False
    return arr        


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")