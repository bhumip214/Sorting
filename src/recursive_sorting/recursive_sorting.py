# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [] * elements
    # TO-DO

    while len(arrA) != 0 and len(arrB) != 0:
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA.remove(arrA[0])
        else:
            merged_arr.append(arrB[0])
            arrB.remove(arrB[0])
    
    if len(arrA) == 0:
        merged_arr = merged_arr + arrB

    else:
        merged_arr = merged_arr + arrA
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
    # 1. While your data set contains more than one item, split it in half
    # 2. Once you have gotten down to a single element, you have also *sorted* that element (a single element cannot be "out of order")
    # 3. Start merging your single lists of one element together into larger, sorted sets
    # 4. Repeat step 3 until the entire data set has been reassembled
def merge_sort( arr ):
    if len(arr) > 1:
       middle = len(arr)//2
       left = merge_sort(arr[:middle])
       right = merge_sort(arr[middle:])
       arr = merge(left, right)
    return arr



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
