class Node(object):
  def __init__(self,key):
    self.key=key
    self.left=None
    self.right=None
  

def printLevelOrder(root):
  Q=[]
  temp_node=root
  while temp_node:
   print temp_node.key,
   if (temp_node.left):
    Q.append(temp_node.left)
   if (temp_node.right):
    Q.append(temp_node.right)
   if Q!=[]:
    temp_node=Q.pop(0)
   else:
    temp_node=None
    
   

root=Node(5)
root.left=Node(4)
root.right=Node(6)
root.left.left=Node(3)
root.left.right=Node(7)
root.left.left.left=Node(2)
root.right.left=Node(1)
root.right.right=Node(8)

printLevelOrder(root)


