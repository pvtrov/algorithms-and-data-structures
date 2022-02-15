# bubblesort

def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def swap(array, right, left):  # zamiaaaaaaaaaana
    temporary_value = array[left]
    array[left] = array[right]
    array[right] = temporary_value
