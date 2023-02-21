# Python program for implementation of Insertion Sort
 
# Function to do insertion sort
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        #add breakpoint here so you can see array changing
        key = arr[i]
 
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 

def main() -> None: 
    arr = [12, 24, 8, 11, 4, 13, 5, 6]
    insertionSort(arr)
    print(arr)
 
if __name__ == '__main__':
    main()