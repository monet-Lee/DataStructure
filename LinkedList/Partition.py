'''将单向链表按某值划分成左边小、中间相等、又变大的形式
1、时间复杂度O(n)、额外空间复杂度O(n):   将链表转换成数组，进行分区，分区后再转回链表.
   注意与partition的区别：（1）存在等于区的处理；（2）pivot是事先指定好的。
2、关键：3个指针的使用，分别指向小于区末尾、大于区末尾、当前判别位置
3、向大于区交换数据时当前判别位置不移动！！

Advance:
时间复杂度为O(n)、额外空间复杂度为O(1):
1、分别生成小于区子链表、大于区子链表、等于区子链表
2、
'''

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    
    # This function counts number of nodes in Linked List
    # iteratively, given 'node' as starting node.
    def getCount(self):
        temp = self.headval # Initialise temp
        count = 0 # Initialise count
 
        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.nextval
        return count

    # 定义只有头指针没有头节点的链表
    def PrintList(self,list1):
        temp = list1
        while(temp):
            print(temp.dataval)
            temp=temp.nextval
    
    # 基于数组生成链表
    def GetListfromArray(self, arr):
        head = Node(arr[0])
        cur = head
        for i in range(1,len(arr)):
            cur.nextval=Node(arr[i])
            cur=cur.nextval
        return head


class Solution():
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        return arr

    def Partition(self, list1, m):
        arr_lst = []
        cnt=0
        while (list1.headval is not None):
            arr_lst.append(list1.headval.dataval)
            list1.headval=list1.headval.nextval
            cnt+=1
        small = -1
        big = cnt
        cur=0
        while(cur != big):
            if arr_lst[cur]<m:    # 小于pivot的值就放到小于区中
                small +=1
                self.swap(arr_lst, small, cur)
                cur +=1
            elif arr_lst[cur]==pivot:
                cur+=1
            else:
                big -=1
                self.swap(arr_lst,big,cur)
        return arr_lst


if __name__ == "__main__":

    arr_init = [9,0,4,3,3,3,5,1]
    list1 = SLinkedList()
    n1 = list1.GetListfromArray(arr_init)
    list1.headval = n1

    pivot = 3
    s = Solution()
    arr = s.Partition(list1, 3)
    head = list1.GetListfromArray(arr)
    list1.PrintList(head)

