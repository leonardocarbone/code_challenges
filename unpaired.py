# Find unpaired value on a odd array consisting of N integers

# Solution 1
lst = [9, 3, 9, 3, 9, 7, 9]

def find_unpaired(list):
  while len(list) >= 0:
    if not list[0] in list[1:]:
      return list[0]
      
  
    list = filter(lambda x: x!= list[0], list)  
    


print find_unpaired(lst)
