# TO-DO: Complete the selection_sort() function below 

def selection_sort( arr ):
    
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
           if arr[j] < arr[smallest_index]:
             smallest_index = j
        
        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    
    # Loop through your array
    # Compare each element to its neighbor
    # If elements in wrong position (relative to each other, swap them)
    # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp  
                is_swapped = True
    return arr
    


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr