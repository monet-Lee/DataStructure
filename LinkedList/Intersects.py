'''判断两个单链表是否相交，长度分别为N、M。注意：单链表只能有1个输出指针（next）
1、时间复杂度（N+M）、额外空间复杂度O(1);
2、判断单链表是否有环，若一个表有环，另一个表无环，则肯定不相交！返回有环链表的第1个入环节点。



'''

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    
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
        temp = list1
        while(temp is not None):
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

    def getLoopNode(self, head):

        return n1

    def intersects(self, list1, list2):
        

if __name__ == "__main__":
    arr_init1 = [9,3,7,6,8,9]
    list1 = SLinkedList()
    head = list1.GetListfromArray(arr_init1)

    s = Solution()
    n1 = s.getLoopNode(head)
    arr = s.intersects(head)

    list1.PrintList(list1.GetListfromArray(arr))

