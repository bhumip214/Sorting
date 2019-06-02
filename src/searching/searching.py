# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  import math 
  while low <= high:
      middle = math.ceil((low + high) / 2)

      # if middle value is equal to target value then return index of middle value
      if arr[middle] == target:
        return middle 

      # if middle value is greater than target value then ignore the right half
      # update variable high with middle - 1
      elif arr[middle] > target:
        high = middle - 1
      
      # if middle value is less than target value then ignore the left half 
      # update variable low with middle + 1
      else:
        low = middle + 1

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2
  # print (f'low = {low}, high= {high}, middle= {middle}')
  
  if len(arr) == 0:
    return -1 # array empty

  # TO-DO: add missing if/else statements, recursive calls
  if arr[middle] == target:
    return middle
  elif arr[middle] > target:
    return binary_search_recursive(arr, target, low, middle - 1)
  elif arr[middle] < target:
    return binary_search_recursive(arr, target, middle + 1, high)  
  else:
    return -1