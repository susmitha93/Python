# directed Dijkstra graph
class Solution():
    def __init__(self,vertices):
        self.V=vertices
        
    def _Getminimum(self,dist,spt,min):
        minindex=0
        for v in range(self.V):
            if dist[v]<min and spt[v]==False:
                min=dist[v]
                minindex=v
        return minindex

    def Dijkstra(self,src,matrix):
        
        import sys 
        min=sys.maxint
        dist=[min]*self.V
        spt=[False]*self.V
        dist[src]=0
        spt[src]=True
        for i in range(self.V):
            u=self._Getminimum(dist,spt,min)
            spt[u]=True

            for v in range(self.V):
                if matrix[u][v]>0 and spt[v]==False:
                    dist[v]=dist[u]+matrix[u][v] 
        self.printdist(dist)

    def printdist(self,dist):
        for v in range(self.V):
            print v,dist[v]

matrix=[[0, 4, 0, 0, 0, 0, 0, 8, 0], 
           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
           [0, 0, 2, 0, 0, 0, 6, 7, 0] 
          ];
obj=Solution(9)
obj.Dijkstra(0,matrix)