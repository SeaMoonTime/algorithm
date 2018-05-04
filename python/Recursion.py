##递归调用示例

##阶乘实现
def fact(x):
    if x==1:
        return 1
    else:
        return x * fact(x-1)

print(fact(5))

##计算一块矩形土地可以分得均匀的最大方块长度
def maxCubeLength(x,y):
    if x<y: ##x<y,交换x,y
        t = x
        x = y
        y = t
    remainder = x%y ##余数
    n = x//y ##倍数
    if remainder==0:
        return y
    else:
        big = y
        small = x-n*y
        return maxCubeLength(big,small)

cubeLength = maxCubeLength(1680,660)
print(cubeLength)

