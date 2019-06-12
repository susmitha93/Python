class Node(object):
  def __init__(self,key):
    self.key=key
    self.left=None
    self.right=None
  
def printLevelOrder(root):
    h=height(root)
    for i in range(1,h+1):
      printthislevel(root,i)

def printthislevel(root,level):
    if not root:
      return
    if level==1:
      print root.key,
    elif level>1:
      printthislevel(root.left,level-1)
      printthislevel(root.right,level-1)

def height(root):
    if not root:
      return 0
    else:
      lheight=height(root.left)
      rheight=height(root.right)

      if lheight>rheight:
        return lheight+1
      else:
        return rheight+1


root=Node(5)
root.left=Node(4)
root.right=Node(6)
root.left.left=Node(3)
root.left.right=Node(7)
root.left.left.left=Node(2)
root.right.left=Node(1)
root.right.right=Node(8)

printLevelOrder(root)
print "Height is "+str(height(root))

