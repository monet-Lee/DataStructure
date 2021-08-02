import random 
from arrays import Array
'''
快速排序：
1、递归的将1个数列分成两个区域，小于区和大于区，直到每个分区只有1个元素

归并排序：

'''

def swap(lyst, i, j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


class QuickSort():

    def quicksort(self, lyst):
        self.quicksortHelper(lyst, 0, len(lyst)-1)

    def quicksortHelper(self, lyst, left, right):
        if left < right:
            pivotLocation = self.partition(lyst, left, right)
            self.quicksortHelper(lyst, left, pivotLocation)
            self.quicksortHelper(lyst, pivotLocation+1, right)
        # print(lyst)

    def partition(self, lyst, left, right):
        middle = (left + right)//2
        pivot = lyst[middle]
        lyst[middle] = lyst[right]
        lyst[right] = pivot
        boundry = left
        for i in range(left, right):
            if lyst[i] < pivot:
                swap(lyst, i, boundry)
                boundry += 1
        swap(lyst, right, boundry)
        return boundry


class MergeSort():  

    def __init__(self):
        pass

    def mergesort(self, lyst):
        copyBuffer = Array(len(lyst))
        self.mergeSortHelper(lyst, copyBuffer, 0, len(lyst)-1)

    def mergeSortHelper(self, lyst, copyBuffer, left, right):
        if left < right:
            middle = (left + right)//2
            self.mergeSortHelper(lyst, copyBuffer, left, middle)
            self.mergeSortHelper(lyst, copyBuffer, middle + 1, right)
            self.merge(lyst, copyBuffer, left, middle, right)
    
    def merge(self, lyst, copyBuffer, left, middle, right):
        i1 = left
        i2 = middle + 1
        for i in range(left, right + 1):
            if i1 > middle:
                copyBuffer[i] = lyst[i2]
                i2 +=1
            elif i2 > right:
                copyBuffer[i] = lyst[i1]
                i1 += 1
            elif lyst[i1] < lyst[i2]:
                copyBuffer[i] = lyst[i1]
                i1 += 1
            else:
                copyBuffer[i] = lyst[i2]
                i2 += 1
        for i in range(left , right + 1):
            lyst[i] = copyBuffer[i]
        # print(lyst)

if __name__ == "__main__":
    lyst = []
    for i in range(9):
        lyst.append(random.randint(1, 100))
    print(lyst)
    print('-----------------')
    
    #快速排序
    # q = QuickSort()
    # q.quicksort(lyst)

    # 归并排序
    m = MergeSort()
    m.mergesort(lyst)


    print(lyst)
