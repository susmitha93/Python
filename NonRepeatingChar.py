class Solution(object):
    def __init__(self):
        self.result=-1
        
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        string=s.lower()
        for i in range(len(string)):
          if (len(string.replace(string[i],""))==len(string)-1):
            self.result=i
            break
        return self.result
   
obj=Solution()
print(obj.firstUniqChar("loveleetcode"))