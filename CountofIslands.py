class Solution(object):
  def __init__(self,obj):
    self.ROW=len(obj)
    self.COL=len(obj[0])
    self.GRID=obj

  def isSafe(self, i, j, visited):
    return (i>=0 and j>=0 and i<self.ROW and j<self.COL and not visited[i][j] and self.GRID[i][j])
    
  def dfs(self, i,j,visited):
    visited[i][j]=True
    adjrow=[-1,0,0,1]
    adjcol=[0,-1,1,0]
        
    for k in range(4):
      if(self.isSafe(i+adjrow[k],j+adjcol[k],visited)):
        self.dfs(i+adjrow[k],j+adjcol[k],visited)
    
  def numIslands(self):
    count=0
    visited = [[False for j in range(self.COL)]for i in range(self.ROW)] 
                  
    for i in range(self.ROW):
      for j in range(self.COL):
        if(self.GRID[i][j]==1 and  visited[i][j]==False):
          self.dfs(i,j,visited)
          count+=1
    return count
    
graph = [[1,1,0,0,0],
[1,1,0,0,0],
[0,0,1,0,0],
[0,0,0,1,1]]
  
  
row = len(graph) 
col = len(graph[0]) 
  
obj = Solution(graph) 
  
print "Number of islands is:"
print obj.numIslands() 
                
        
        