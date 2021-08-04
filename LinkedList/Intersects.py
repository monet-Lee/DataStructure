'''判断两个单链表是否相交，长度分别为N、M。注意：单链表只能有1个输出指针（next）
1、时间复杂度（N+M）、额外空间复杂度O(1);
2、判断单链表是否有环，若一个表有环，另一个表无环，则肯定不相交！返回有环链表的第1个入环节点。
3、无环链表相交只能是Y字型相交，只要出现相同dataval的节点，这各节点就是相交的第1个节点，且后续节点全部相交
4、有环链表是否相交分三种情况：
（1）Y字型，链表相交在环外，此时入环首节点必定相同。其他2种情况，入环的首节点必定不同。
（2）两个有环链表没有相交点
（3）相交在环内，两个链表从环上不同的位置接入，环必须是相同的。
     如链1：1-2-3-4-5-6-...-4-5-6；链2：7-8-5-6-4-...-5-6-4。

'''

class Node:
    def __init__(self, dataval):
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
        while(temp != None):
            print(temp.dataval)
            temp=temp.nextval
        
    # 基于数组生成有环单链表
    def GetListfromArrayLoop(self, arr):
        head = Node(arr[0])
        cur = head
        for i in range(1,len(arr)):
            cur.nextval=Node(arr[i])
            cur=cur.nextval
        cur.nextval = head.nextval.nextval
        return head

    def GetListfromArrayLoop2(self, arr):
        head = Node(arr[0])
        cur = head
        for i in range(1,len(arr)):
            cur.nextval=Node(arr[i])
            cur=cur.nextval
        cur.nextval = head.nextval.nextval.nextval
        return head
    
    # 基于数组生成无环单链表
    def GetListfromArray(self, arr):
        head = Node(arr[0])
        cur = head
        for i in range(1,len(arr)):
            cur.nextval=Node(arr[i])
            cur=cur.nextval
        return head

class Solution():

    def getLoopNode(self, head):
        if (head == None) or (head.nextval == None) or(head.nextval.nextval == None):
            return None
        slow = head
        fast = head
        fast = fast.nextval.nextval
        slow = slow.nextval
        while(fast != slow):
            if(fast.nextval == None or fast.nextval.nextval == None):
                return None
            fast = fast.nextval.nextval
            slow = slow.nextval
            if fast == None:
                return None
        fast = head
        while(fast!=slow):
            fast = fast.nextval
            slow = slow.nextval
        return slow
    
    def noloop(self, head1, head2):
        cur1 = head1.headval
        cur2 = head2.headval
        n=0
        while cur1.nextval != None:
            n +=1
            cur1 = cur1.nextval
        while cur2.nextval != None:
            n-=1
            cur2=cur2.nextval
        if(cur1.dataval != cur2.dataval):
            return None
        n1 = head1.headval if n>0 else head2.headval
        n2 = head1.headval if n1 == head2.headval else head2.headval
        n = abs(n)
        while (n!=0):
            n-=1
            n1 = n1.nextval
        while n1.dataval != n2.dataval:
            n1=n1.nextval
            n2=n2.nextval
        return n1.dataval

    def intersects(self, list1, list2, lpf1, lpf2):
        # 第一种情况：在环外相交，类似无环的Y字相交
        if (lpf1.dataval==lpf2.dataval):
            cur1=list1.headval
            cur2 = list2.headval
            n=0
            while cur1.nextval.dataval != lpf1.dataval:
                cur1=cur1.nextval
                n+=1
            while cur2.nextval.dataval != lpf2.dataval:
                cur2=cur2.nextval
                n-=1
            n1 =list1.headval if n>0 else list2.headval
            n2 = list1.headval if n1.dataval==list2.headval.dataval else list2.headval
            n=abs(n)
            while n!=0:
                n-=1
                n1=n1.nextval
            while n1.dataval != n2.dataval:
                n1=n1.nextval
                n2=n2.nextval
            return n1.dataval
        else:
            loop_dt=lpf1.dataval
            while lpf1.nextval.dataval != loop_dt:
                lpf1 = lpf1.nextval
                if lpf1.dataval == lpf2.dataval:
                    return lpf1.dataval
            return None
        

if __name__ == "__main__":
    arr_init1 = [9,3,7,6,8,9]
    arr_init2 = [1,2,3,8,9,7,6]
    list1 = SLinkedList()
    list2 = SLinkedList()
    n1 = list1.GetListfromArrayLoop(arr_init1)
    n2 = list2.GetListfromArrayLoop2(arr_init2)
    list1.headval=n1
    list2.headval = n2

    s = Solution()
    lpf1 = s.getLoopNode(list1.headval)
    lpf2 = s.getLoopNode(list2.headval)
    if (not lpf1 and not lpf2):
        # 无环单链表的相交节点
        ntrscts = s.noloop(list1, list2)
    elif (lpf1 and lpf2):
        # 有环单链表的相交
        ntrscts = s.intersects(list1, list2, lpf1, lpf2)
    else:
        ntrscts=None
    print("相交节点为： ",ntrscts)
