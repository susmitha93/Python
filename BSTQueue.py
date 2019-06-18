class Node(object):
  def __init__(self,key):
    self.key=key
    self.left=None
    self.right=None
  

def printLevelOrder(root):
  Q=[]
  Q.append(root)
  while Q!=[]:
   print Q[0].key,
   if (Q[0].left):
    Q.append(Q[0].left)
   if (Q[0].right):
    Q.append(Q[0].right)
   Q.pop(0)
   
    
   

root=Node(5)
root.left=Node(4)
root.right=Node(6)
root.left.left=Node(3)
root.left.right=Node(7)
root.left.left.left=Node(2)
root.right.left=Node(1)
root.right.right=Node(8)

printLevelOrder(root)


