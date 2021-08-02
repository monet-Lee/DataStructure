'''将单向链表按某值划分成左边小、中间相等、又变大的形式

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
    
    def PrintList(self,list1):
        temp = list1.headval
        while(temp):
            print(temp.dataval)
            temp=temp.nextval

class Solution():
    def Partition(self, list1, m):
        pass      


if __name__ == "__main__":
    n1 = Node(9)
    n2 = Node(0)
    n3 = Node(4)
    n4 = Node(5)
    n5 = Node(1)
    n1.nextval = n2
    n2.nextval = n3
    n3.nextval = n4
    n4.nextval = n5
    list1 = SLinkedList()
    list1.headval = n1

    pivot = 3
    s = Solution()
    list1.PrintList(list1)
    # print(s.Partition(list1, 3))

