class Solution(object):
  def __init__(self,array):
    self.output=[]
    self.array=array
    self.maxsum=self.array[0]
    self.start=0
    self.end=0
  
  def Findindices(self):
    currmax=self.array[0]
    currstart=0
    currend=0
    for i in range (1,len(self.array)):
      if(self.array[i]>self.array[i]+currmax):
        currmax=self.array[i]
        currstart=i
        currend=i
      else:
        currmax= self.array[i]+currmax
        currend=i    
      if(currmax>self.maxsum):
        self.maxsum=currmax
        self.start=currstart
        self.end=currend
    return "Started at index {} and ended at index {} with maxsum of {}".format(self.start,self.end,self.maxsum)

obj=Solution([-2,-1,12,-3,-4])
print(obj.Findindices());

    

