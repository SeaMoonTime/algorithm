## 快速排序
def quicksort(array):
    if len(array) < 2:
        return array  ##基线条件：数组为空或只包括一个元素的数组是有序的
    else:
        baseIndex = len(array)//2
        pivot = array.pop(baseIndex) ##递归条件：基准值,数组中间值做基准值，将改值从数组中取出
        less = [i for i in array if i<=pivot] ##由所有小于等于基准值的元素组成的子数组
        greater = [i for i in array if i>pivot] ##由所有大于基准值的元素组成的子数组
        return quicksort(less) + [pivot] + quicksort(greater)


sortedArray = quicksort([13,15,12,7,2,9,1,11,3,5,3,6,11,7,2,16,8,19,22,17,16,14,12])
print(sortedArray)

