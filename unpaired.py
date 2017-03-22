# Find unpaired value that occurs in odd number of elements.

# Solution 1
def find_unpaired(list):
  list.sort()
  
  index = 0
  while index < len(list)-1:
    if list[index] != list[index+1]:
      return list[index]
      
    index+=2
  
  return list[index]


print find_unpaired([3, 3, 9, 9, 10])
print find_unpaired([5, 3, 5])
print find_unpaired([42])
print find_unpaired([5, 2, 3, 1, 2, 5, 3])
print find_unpaired([5, 2, 3, 4, 4, 5, 3])
