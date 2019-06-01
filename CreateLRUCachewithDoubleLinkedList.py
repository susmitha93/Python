class Node:
  def __init__(self,key,value,next=None,prev=None):
    self.key=key
    self.value=value
    self.next=None
    self.prev=None

class LRUCache(object):
  def __init__(self,capacity):
    self.capacity=capacity
    self.head=Node(0,0)
    self.tail=Node(0,0)
    self.dict=dict()
    self.head.next=self.tail
    self.tail.prev=self.head

  def remove(self,node):
    prev=node.prev
    next=node.next
    prev.next=next
    next.prev=prev

  def add(self,node):
    prev=self.tail.prev
    prev.next=node
    self.tail.prev=node
    node.prev=prev
    node.next=self.tail

  def get(self,key):
    if key in self.dict:
      node=self.dict[key]
      self.remove(node)
      self.add(node)
      return node.value
    else:
      return  -1

  def put(self,key,value):
    node=Node(key,value)
    if key in self.dict:
      self.remove(self.dict[key])
    self.add(node)
    self.dict[key]=node
    
    if(len(self.dict)>self.capacity):
      node=self.head.next
      self.remove(node)
      del self.dict[node.key]
    
  
  def printLRU(self):
    for key in self.dict:
      print("{}:{}").format(key,self.dict[key].value)

cache=LRUCache(2)
cache.put(1, 1);
cache.put(2, 2);
print(cache.get(1));       # returns 1
cache.put(3, 3);    # evicts key 2
print(cache.get(2));       # returns -1 (not found)
cache.put(4, 4);    #evicts key 1
print(cache.get(1));       # returns -1 (not found)
print(cache.get(3));       # returns 3
print(cache.get(4));       # returns 4

