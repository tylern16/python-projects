
def find_max(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max