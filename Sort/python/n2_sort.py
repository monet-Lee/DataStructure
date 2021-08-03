import random
'''n个数据排序
选择排序：
1、O(n2)、O(n2)、O(n2)
2、每次从数列中查找到最小的元素，插入到有序数列的末尾。


以下2个时间复杂度平均、最差、最好：O(n2)、O(n2)、O(n)
冒泡排序：
1、每次冒泡，从第一个位置开始，相邻元素比较。较大的值继续向后比较，且比较次数都减1；
2、最好时间复杂度为O(n)的计算方式：设置交换标志，当数列正序，
   交换标志不发生变化，此时为最优时间复杂度。

插入排序：
1、初始排好序的数列只有首元素，从第2个元素开始依次将剩余的数列插入到排好序的数列中，
   每次插入新的元素后，数列仍然有序，直到插入最后一个元素，结束。

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
                minIndex = j        
        swap(lyst, i, minIndex)
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
                lyst[j + 1] = lyst[j]    #将较大的元素向后移一位，将插入位置空出来
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
