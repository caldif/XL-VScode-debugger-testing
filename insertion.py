# Python program for implementation of Insertion Sort
 
# Function to do insertion sort
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        #add breakpoint here so they can see array changing
        #then change to hit and or conditional breakpoint
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        #breakpoint here to show how using the step command takes it line by line
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 

def main() -> None: 
    arr = [12, 24, 8, 11, 4, 13, 5, 6]
    insertionSort(arr)
    for i in range(len(arr)):
        print(arr[i])
 
if __name__ == '__main__':
    main()