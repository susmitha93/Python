def twoSum(nums, target):
  num=sorted(nums)
  bol=False
  for i in range(len(nums)-1,0,-1):
    for j in range(len(nums)-2,-1,-1):
      sum=num[i]+num[j];
      if (sum==target):
        bol=True
        return nums.index(num[j]),nums.index(num[i])
  if bol==False:
    return "No pairs"
       
  

print twoSum([60,40,10,20,90],100)



        