'''判断是否为回文
1、使用快指针cur、慢指针R时，注意奇数个节点、偶数个节点是如何区别处理的
[通过控制入栈元素，处理奇、偶节点数量]
解析：
cur指针经过n次移动后，落在最后一个节点上（共2n+1个节点）或倒数第2个节点上（共2(n+1)个节点）；
此时，R指针落在第n+1个节点上，巧妙从第n+2个节点开始入栈计算回文，同时满足奇数、偶数数量的节点。

2、进阶：额外空间复杂度O(1)

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

class Solution():
    def PalindromeDetecte(self, list1):
        tstck = []
        R = list1.headval
        cur = list1.headval
        while(cur.nextval!=None and cur.nextval.nextval != None):
            R = R.nextval
            cur = cur.nextval.nextval
        while(R.nextval !=None):
            tstck.append(R.nextval.dataval)
            R = R.nextval
        while(len(tstck)!=0):
            dt_val = tstck[len(tstck)-1]
            tstck.pop()
            if(list1.headval.dataval != dt_val):
                return False
            list1.headval = list1.headval.nextval
            return True



if __name__ == "__main__":
    n1 = Node("1")
    n2 = Node("2")
    n3 = Node("3")
    n5 = Node("2")
    n6 = Node("1")
    n1.nextval = n2
    n2.nextval = n3
    n3.nextval = n5
    n5.nextval = n6
    list1 = SLinkedList()

    list1.headval = n1
    s = Solution()
    print(s.PalindromeDetecte(list1))

