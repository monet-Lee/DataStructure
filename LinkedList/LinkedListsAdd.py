'''两个单链表生成相加链表，如9-3-7 + 6-3 ——>1-0-0-0
1、将两个链表分别存到栈中，设置进位标志ca
2、亮点：（1）逆序一维数组：arr[::-1]；（2）巧妙使用整除、取余操作。


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
    def add(self, list1, list2):
        arr=[]
        stack1 = []
        stack2 = []
        ca = 0
        while (list1 is not None):
            stack1.append(list1.dataval)
            list1 = list1.nextval
        while(list2 is not None):
            stack2.append(list2.dataval)
            list2 = list2.nextval

        while(len(stack1)!=0 or len(stack2)!=0):
            temp1 = 0 if len(stack1)==0 else stack1.pop()
            temp2 = 0 if len(stack2)==0 else stack2.pop()

            sum_v = temp1+temp2+ca
            arr.append(sum_v%10)
            ca=sum_v//10
        if ca==1:
            arr.append(1)

        return arr[::-1]



if __name__ == "__main__":
    arr_init1 = [9,3,7]
    arr_init2 = [6,3]
    list1 = SLinkedList()
    head1 = list1.GetListfromArray(arr_init1)
    head2 = list1.GetListfromArray(arr_init2)

    s = Solution()
    arr = s.add(head1, head2)
    list1.PrintList(list1.GetListfromArray(arr))

