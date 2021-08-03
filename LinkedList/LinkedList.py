'''翻转部分链表
1、找到from-1位置和to+1位置
2、将from位置连到to+1位置
3、from位置到to位置依次翻转
4、将from-1位置链接到to位置
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

class Solution():
    def reverse(self, list1, _from, _to):
        fpre = Node()
        tpos = Node()
        loc_id = 0
        # start如果为首节点，fpre保持为None,此时反转包含头结点
        node_cur = list1.headval
        while(node_cur!=None):
            loc_id +=1
            fpre = node_cur if loc_id==_from-1 else fpre
            tpos = node_cur if loc_id==_to+1 else tpos
            node_cur=node_cur.nextval
        if(_from<0 or _to>loc_id or _from>_to):
            return list1
        
        node_strt = list1.headval if fpre.nextval==None else fpre.nextval
        node_scnd = node_strt.nextval
        node_strt.nextval=None if tpos.dataval==None else tpos
        node_next = Node()
        while(node_scnd!=None and node_scnd != tpos):
            node_next = node_scnd.nextval
            node_scnd.nextval=node_strt
            node_strt = node_scnd
            node_scnd = node_next
        # 如果不是头结点，from位置连接到to+1位置
        if fpre.nextval!=None:
            fpre.nextval=node_strt
        else:
            list1.headval = node_strt
        return list1


if __name__ == "__main__":
    arr_init = [9,0,4,3,3,3,5,1]
    list1 = SLinkedList()
    n1 = list1.GetListfromArray(arr_init)
    list1.headval = n1

    s = Solution()
    list1.PrintList(s.reverse(list1, 2, 5))

