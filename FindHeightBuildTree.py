class Node():
  def __init__(self,key):
    self.key=key
    self.left=None
    self.right=None

def BuildTree(l):
  root=None
  curnode=None
  nodelib={}
  for i in range(len(l)):
    nodelib[i]=Node(i)

  for i in range(len(l)):
    if l[i]==-1:
      root=nodelib[i]
    else:
      curnode=nodelib[l[i]]
      if curnode.left:
        curnode.right=nodelib[i]
      else:
        curnode.left=nodelib[i]
 
  printtree(root)
  return root

def printtree(root):
  Q=[]
  Q.append(root)
  while Q:
    if Q[0]:
      print Q[0].key,
      Q.append(Q[0].left)
      Q.append(Q[0].right)
    Q.pop(0)

def Height(l):
  root=BuildTree(l)
  print "Height is: "+str(findheight(root))

def findheight(root):
  if root==None:
    return 0
  lheight=findheight(root.left)
  rheight=findheight(root.right)

  if lheight>rheight:
    return lheight+1
  else:
    return rheight+1

    
l=[1,5,5,2,2,-1,3]
Height(l)



