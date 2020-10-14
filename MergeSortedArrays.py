def mergeSortedArrays(array_one, array_two):
  big_array = []
  i = 0
  j = 0
  while i < len(array_one) and j < len(array_two):
    if array_one[i] <= array_two[j]:
      big_array.append(array_one[i])
      i += 1
    else:
      big_array.append(array_two[j])
      j += 1
  
  return big_array+array_one[i:]+array_two[j:]


print(mergeSortedArrays([0,3,4,31], [4,6,30]))
