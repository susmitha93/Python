l=[1, 5, 5 ,2 ,2 ,-1 ,3]
rootval=l.index(-1)
def FindTreeDepth(l):
  ret=[]
  for i in range(len(l)):
    ret.append(depth(i))
  print sorted(ret)[len(ret)-1]

def depth(i):
  if i==rootval:
    return 1
  else:
    return depth(l[i])+1    

  

FindTreeDepth(l)
