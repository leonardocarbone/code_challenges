# Find longest sequence of zeros in binary representation of an integer.

# Solution 1

# Convert decimal integer to a binary string. It's possible to use a built-in function bin() as well
def to_bin(value):
  
  bin_str = ""
  while (value!=0):
    bin_str = str(value%2) + bin_str
    value/=2  

  print "Binary sequence", bin_str  
  return bin_str

def check_longest(binary_str):
  longest_gap = temp_gap = 0
  
  for b in binary_str:
    if b == "0":
      temp_gap+=1
    else:
      if temp_gap > longest_gap:
        longest_gap = temp_gap
        
      temp_gap = 0
    
  return longest_gap
  
n = int(input("Enter integer value:"))
print check_longest(to_bin(n))
