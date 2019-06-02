def twoSum(nums, target):
  num=sorted(nums)
  bol=False
  for i in range(len(num)-1,0,-1):
    for j in range(len(num)-2,-1,-1):
      sum=num[i]+num[j];
      if (sum==target):
        bol=True
        return nums.index(num[i]),nums.index(num[j])
  if bol==False:
    return []

print twoSum([180,40,110,20,90],200)



        