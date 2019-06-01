# GCD of more than two (or array) numbers 
  
# Function implements the Euclidian  
# algorithm to find H.C.F. of two number 
def find_gcd(x, y): 
  while(y): 
    x, y = y, x % y 
  return x 
     
# Driver Code         
l = [0,0,0,0,0,0,0,9]
if(len(l)>2):
  gcd = find_gcd(l[0],l[1])
  for i in range(2, len(l)): 
    gcd=find_gcd(gcd,l[i])
else:
    gcd = find_gcd(l[0],l[1])
print(gcd) 
  
