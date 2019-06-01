def cellcompete(state,days):
  if(days%14==0 or not (1 in state) ): 
    state=state
  else:
    days=days%14
    for z in range (days):
      Nextstate=[];
      for j in range(n):
        if j==0:
          Nextstate.insert(j,state[j+1]);
        elif j==n-1:
          Nextstate.insert(j,state[j-1]);
        else:
          Nextstate.insert(j,xor(state[j-1],state[j+1]));
      state=Nextstate;
  return state;
pass

def xor(a,b):
  if(a!=b):
    c=1
  else:
    c=0
  return c;
state=[]
state=input("While Active is 1 and Inactive is 0. Please enter list of 8 statuses in this format--> [1,0,1,0,1,1,0,1] > ");
n=len(state)
if(n>8):
  state=input("The number of statuses should be 8. Please enter again:")
days= input("Enter how many days after you want to see the status: ");
state=cellcompete(state,days);
print(state);
