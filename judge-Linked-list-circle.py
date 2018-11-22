class Node():
    def __init__(self,node):
        self.node = node 
        self.next = None
def loop(head):
    slow = head
    fast = head
    loop = False
    if head == None:
        return False
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        print(slow.node,fast.node )
        if slow == fast:
            loop = True
            break

    if loop == True:
        slow = head
        while slow!= fast:
            fast = fast.next
            slow = slow.next
        return slow

    print("Not Exist")
        
        
    return False 
  
if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2
    print(loop(node1).node)
                    
