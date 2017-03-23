def rotate(arr, rotate_value):
  if len(arr) == 0: return arr 
  
  last = 0
  n = len(arr)
  temp = []
  for x in range(0, rotate_value):
    last = arr[n-1]
    temp = arr[0:n-1]
    
    arr[0] = last
    for index in range (0,len(temp)):
      arr[index+1] = temp[index]
      
  
  return arr
    
to_rotate = range(5)
print rotate(to_rotate,1)
