import random
'''n个数据排序
选择排序：

冒泡排序：
1、每次冒泡，比较次数都减1；
2、最有时间复杂度为O(n)。计算方式：设置交换标志，当数列正序，
   交换标志不发生变化，此时为最优时间复杂度。

插入排序：

'''

def swap(lyst, i, j):
    """
    param:
    lyst {list}:
    i {int}:
    j {int}:

    """
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


def selectionSort(lyst):

    for i in range(len(lyst) - 1):
        minIndex = i
        for j in range(i+1, len(lyst)):
            if lyst[j] < lyst[minIndex]:
                swap(lyst, j, minIndex)

    print(lyst)


def bubbleSort(lyst):

    for i in range(len(lyst), 0, -1):
        for j in range(1, i):            
            if lyst[j - 1] > lyst[j]:
                swap(lyst, j - 1, j)
                j += 1
            else:
                j += 1
    print(lyst)


def insertSort(lyst):

    for i in range(1, len(lyst)):
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            if lyst[j] >= itemToInsert:
                lyst[j + 1] = lyst[j]    
                j -= 1
            else:
                break
        lyst[j + 1] = itemToInsert
    print(lyst)



if __name__ == "__main__":
    lyst = []
    for i in range(10):
        lyst.append(random.randint(1, 100))
    print(lyst)
    print('-----------------')
    # 选择排序
    selectionSort(lyst)

    # 冒泡排序
    # bubbleSort(lyst)

    # 插入排序
    # insertSort(lyst)
