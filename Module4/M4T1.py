def merge_sort(collection):
    def merge(left,right):
        ordered = []
        
        while left and right:
            ordered.append((left if left[0] <= right[0] else right).pop(0))
        return ordered + left + right
    length = len(collection)
    if length == 1:
        return collection
    center = length // 2
    left = merge_sort(collection[:center])
    right = merge_sort(collection[center:])
    return merge(left,right)
array = input("input array:").split()
for i in range(0,len(array)):
    array[i]=int(array[i])
array = merge_sort(array)
print(array)