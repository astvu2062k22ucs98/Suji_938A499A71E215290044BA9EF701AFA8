def linear_search(array,x): 
  for i,element in enumerate(array):
   if element == x:
      return i
  return -1
  
array = [2,4,0,1,9]
x = 1
result=linear_search(array,x)

if result == -1:
   print("Element not found") 
else:
   print(f"Element found at index: {result}")