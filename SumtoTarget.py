class Solution(object):
    def __init__(self):
        self.output=[];
        
    
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                sum=nums[i]+nums[j];
                if (sum==target):
                    self.out(i,j);
                    return self.output;
             
    def out(self,i,j):
        self.output.insert(0,i);
        self.output.insert(1,j);
    
      
    
obj=Solution();
print(obj.twoSum([2,5,5,11],10));
        