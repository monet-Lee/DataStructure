'''将单链表的每K个节点之间逆序
1、利用栈实现，时间复杂度为O(N)，额外空间复杂度为O(k)
2、包含头指针的第一组数据，需单独区分处理！

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

class Solution(Node):

    def each_group(self, stack_dt, left, right):
        cur = stack_dt.pop()
        if left!=None:
            left = cur
        while len(stack_dt)!=0:
            next_n = stack_dt.pop()
            cur.nextval=next_n
            cur = cur.nextval
        cur.nextval=right
        return cur

    def revese_by_k(self, list1, k):
        if k<2:
            return list1
        newHead = list1
        cur=list1.headval
        pre = list1.headval
        cnt=0
        temp=[]
        while cur != None:
            next_n = cur.nextval
            temp.append(Node(cur.dataval))
            cnt+=1
            if(cnt==k):
                pre = self.each_group(temp, pre, next_n)
                cnt=0
                newHead.headval = cur if newHead.headval.dataval==list1.headval.dataval else newHead.headval
            cur=next_n
        return newHead



if __name__ == "__main__":
    arr_init = [9,0,4,3,3,3,5,1]
    list1 = SLinkedList()
    n1 = list1.GetListfromArray(arr_init)
    list1.headval = n1
    s = Solution()
    k=3
    print(s.revese_by_k(list1, k))

