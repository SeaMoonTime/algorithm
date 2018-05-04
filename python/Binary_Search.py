## 二分查找示例
def binary_search(list,item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess==item:
            return mid
        if guess>item:
            high = mid-1
        else:
            low = mid+1
    return None

mylist = [1,5,9,11,24,49,91]
index = binary_search(mylist,5)
print(index)



    