class Solution(object):
    def __init__(self):
        self.dic={0:"",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten"
        ,11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",         18:"Eighteen",19:"Nineteen",20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety",100:"Hundred",1000:"Thousand"
                    ,1000000:"Million",1000000000:"Billion"}
     
    def three(self,num):

        if len(num)==3:
            if(num[1]==1):
                return  ("{} {} {}").format(self.dic[num[0]],self.dic[100],self.dic[num[1]*10+num[2]])
            else:
                if(num[1]==0 and num[2]==0):
                    return ("{} {} {} {}").format(self.dic[num[0]],self.dic[100],self.dic[num[1]*10],self.dic[num[2]])
                else:
                    return ("{} {} {} {}").format(self.dic[num[0]],self.dic[100],self.dic[num[1]*10],self.dic[num[2]])
        elif len(num)==2:
            if(num[0]==1):
                return ("{}").format(self.dic[num[0]*10+num[1]])
            else:
                return("{} {}").format(self.dic[num[0]*10],self.dic[num[1]])
        elif len(num)==1:
            return (self.dic[num[0]])
    
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        intlist=map(int,str(num))
        l=len(intlist)
        if num==0: return "Zero"
        if l<4:
            return self.three(intlist)
        elif l==4:
            return ("{} {} {}").format(self.three([intlist[0]]),self.dic[1000],self.three(intlist[1:]))
        elif l==5:
            return ("{} {} {}").format(self.three(intlist[0:2]),self.dic[1000],self.three(intlist[2:]))
        elif l==6:
            return ("{} {} {}").format(self.three(intlist[0:3]),self.dic[1000],self.three(intlist[3:]))
        elif l==7:
            return ("{} {} {} {} {}").format(self.three([intlist[0]]),self.dic[1000000],self.three(intlist[1:4]),self.dic[1000],self.three(intlist[4:]))
        elif l==8:
            return ("{} {} {} {} {}").format(self.three(intlist[0:2]),self.dic[1000000],self.three(intlist[2:5]),self.dic[1000],self.three(intlist[5:]))
        elif l==9:
            return ("{} {} {} {} {}").format(self.three(intlist[0:3]),self.dic[1000000],self.three(intlist[3:6]),self.dic[1000],self.three(intlist[6:]))
        elif l==10:
            return ("{} {} {} {} {} {} {}").format(self.three([intlist[0]]),self.dic[1000000000],self.three(intlist[1:4]),self.dic[1000000],self.three(intlist[4:7]),self.dic[1000],self.three(intlist[7:]))
        
       
obj=Solution()
print(obj.numberToWords(1234567891))
            
        
        

 
        