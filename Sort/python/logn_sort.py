import random 
'''
快速排序：
1、递归的将1个数列分成小于区、等于区、大于区，直到每个分区只有1个元素；
2、每次分区，都将数列的首元素当作分区标准；

归并排序：
1、
'''

def swap(lyst, i, j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


class QuickSort():

    def quicksort(self, S):
        # 基线条件
        if len(S) < 2:
            return S
        else:
            pivot = S[0]
            greater = [i for i in S[1:] if i > pivot]
            less = [i for i in S[1:] if i < pivot]
            equal = [i for i in S[1:] if i == pivot]
            return self.quicksort(less) + equal + [pivot] + self.quicksort(greater)


class MergeSort():  

    def mergesort(self, seq):
        if len(seq) <= 1:
            return seq
        mid = len(seq)//2  
        
        left = self.mergesort(seq[:mid])  # divide 分割
        right = self.mergesort(seq[mid:])
        
        return self.merge(left, right) # merge 合并

    def merge(self, left, right):
        result = []  
        i = 0  
        j = 0
        
        while i < len(left) and j < len(right): 
            if left[i] <= right[j]: # 比较大小，排序
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]  # 这两行的处理，是防止left或者right的一边处理完毕，另一边还没有处理完毕。把剩余部分直接放入result中。
        result += right[j:]
        return result

if __name__ == "__main__":
    lyst = []
    for i in range(9):
        lyst.append(random.randint(1, 100))
    print(lyst)
    print('-----------------')
    left = 0
    right = len(lyst) -1

    #快速排序
    # q = QuickSort()
    # S = q.quicksort(lyst)
    # for i in range(len(S)):
    #     print(S[i],end = ' ')

    # 归并排序
    m = MergeSort()
    print(m.mergesort(lyst))
