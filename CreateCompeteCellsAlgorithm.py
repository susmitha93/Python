import sys

def cellcompete(state,days):

for z in range (days):

    n=8;

    Nextstate=[];

    if state[1]==0:

    Nextstate.insert(0,0);

    else:

    Nextstate.insert(0,1);

if state[n-2]==0:

Nextstate.insert(n-1,0);

else:

Nextstate.insert(n-1,1);

for j in range (1,n-1):

if (state[j-1]==0 and state[j+1]==0) or (state[j-1]==1 and state[j+1]==1):

Nextstate.insert(j,0);

else:

Nextstate.insert(j,1);

state=Nextstate;

return state;

pass

 

n=8;

state=[];

for i in range(1,n+1):

a= input("Enter state for cell number " +str(i)+":");

state.append(a);

days= input("Enter how many days after you want to see the status: ");

try:

state=cellcompete(state,days);

print(state);

except:

print ("Error!!!!!! Please enter the status as binary input: that is 0 or 1");