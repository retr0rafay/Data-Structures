def mergeUnsortedArrays(array1, array2):
  bigArray = array1 + array2

  for i in range(len(bigArray)):
    for j in range(i + 1, len(bigArray)):
      if bigArray[i] >= bigArray[j]:
        num = bigArray[i]
        bigArray[i] = bigArray[j]
        bigArray[j] = num
        
      
  return bigArray

print(mergeUnsortedArrays([4,0,3,31,5], [4,32,6]))
