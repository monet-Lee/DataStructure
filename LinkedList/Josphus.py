'''环形单链表约瑟夫问题
1、注意环形单链表的定义
2、注意进阶中规律公式
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
    def JosphusKill(self, list1, m):
        if(list1.headval.dataval is None or list1.headval.nextval == list1.headval or m<1):
            return list1
        last = list1.headval
        while(last.nextval != list1.headval):
            last = last.nextval
        cnt = 0
        while(list1.headval!=last):
            cnt +=1
            if(cnt== m):
                last.nextval = list1.headval.nextval
                cnt =0
            else:
                last = last.nextval
            list1.headval = last.nextval
        return list1
    
    # def JosphusKillAdvanced(self, list1, m):



if __name__ == "__main__":
    n1 = Node("1")
    n2 = Node("2")
    n3 = Node("3")
    n4 = Node("4")
    n5 = Node("5")
    n1.nextval = n2
    n2.nextval = n3
    n3.nextval = n4
    n4.nextval = n5
    list1 = SLinkedList()

    list1.headval = n1
    n5.nextval = n1
    s = Solution()
    print(s.JosphusKill(list1, 3).headval.dataval)
    # print(s.JosphusKillAdvanced(list1, 3).headval.dataval)

