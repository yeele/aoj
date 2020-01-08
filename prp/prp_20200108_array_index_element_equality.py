
import sys
def index_equals_value_search(arr):
    # [-5,0,2,3,10,29]
    mini = [sys.maxsize] # 3
    def rec(i, j): # 0, 6
        if i < j:
            pivot = i + ((j-i) // 2) # 0 + ((6-0)//2) => 3
            if arr[pivot] == pivot:  # 3 == 3: Match!
                mini[0] = min(pivot, mini[0])
                rec(i, pivot)
            elif arr[pivot] > pivot: # discard later part
                rec(i, pivot)
            else:
                rec(pivot+1, j)  # 1+1= 2, 3

    rec(0, len(arr))
    return -1 if mini[0] == sys.maxsize else mini[0]


arr = [-5,0,2,3,10,29]
print(index_equals_value_search(arr))
'''
  [-8, 0, 2, 5, 9, 10, 15]
  [ 0, 1, 2, 3, 4, 5,   6]
  
                ^  
  pseudocode
  mini = -sys.maxsize
  i, j # start and end j is not included 
  pviot = i + ((j-i) // 2)
  
  if arr[pivot] == p: mini = min(p, mini)
  elif arr[pivot] > p: # discard later part
    rec(arr, i, pivot)
  else:
    rec(arr, pivot+1, j)
  return mini      
  
  
  function indexEqualsValueSearch(arr):
    start = 0
    end = arr.length - 1

    while (start <= end):
        i = round((start+end)/2)
        if (arr[i] - i < 0):
            start = i+1
        else if (arr[i] - i == 0) and ((i == 0) or (arr[i-1] - (i-1) < 0)):
            return i
        else:
            end = i-1

    return -1
  
  
'''


import sys
def index_equals_value_search(arr):
    # [-5,0,2,3,10,29]
    mini = [sys.maxsize] # 3
    def rec(i, j): # 0, 6
        if i < j:
            pivot = i + ((j-i) // 2) # 0 + ((6-0)//2) => 3
            if arr[pivot] == pivot:  # 3 == 3: Match!
                mini[0] = min(pivot, mini[0])
                rec(i, pivot)
            elif arr[pivot] > pivot: # discard later part
                rec(i, pivot)
            else:
                rec(pivot+1, j)  # 1+1= 2, 3
    rec(0, len(arr))    
    return -1 if mini[0] == sys.maxsize else mini[0]


arr = [-5,0,2,3,10,29]
print(index_equals_value_search(arr))
'''
  [-8, 0, 2, 5, 9, 10, 15]
  [ 0, 1, 2, 3, 4, 5,   6]
  
                ^  
  pseudocode
  mini = -sys.maxsize
  i, j # start and end j is not included 
  pviot = i + ((j-i) // 2)
  
  if arr[pivot] == p: mini = min(p, mini)
  elif arr[pivot] > p: # discard later part
    rec(arr, i, pivot)
  else:
    rec(arr, pivot+1, j)
  return mini      
  
  
  function indexEqualsValueSearch(arr):
    start = 0
    end = arr.length - 1

    while (start <= end):
        i = round((start+end)/2)
        if (arr[i] < i):
            start = i+1
        else if (arr[i] - i == 0) and ((i == 0) or (arr[i-1] - (i-1) < 0)):
            return i
        else:
            end = i-1
    return -1
  
'''