def twoSum(array, target):
    array_of_indices = []
    i = 0
    while i < len(array):
        if len(array_of_indices) == 2:
            break
        if target - array[i] in array and array[i] == target - array[i] and array.count(array[i]) == 1:
            i += 1
            continue
        if target - array[i] in array:
            array_of_indices.append(i)
        i += 1
    return array_of_indices


print(twoSum([3, 2, 4], 6))

# The runtime could definitely be improved. A hashmap or dictionary would be of better use for improving the runtime.
