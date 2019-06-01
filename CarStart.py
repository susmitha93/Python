command="";
i=0
j=0
while(True):
  command=raw_input("enter command: ").lower(); 
  if command=="start" and i!=1:
    print("Car started...");
    i=1
  elif command=="start" and i==1:
    print("Car is already started")
  elif command=="stop" and j!=2:
    print("Car Stopped...");
    j=2
  elif command=="stop" and j==2:
    print("Car is already stopped")
  elif command=="quit":
   print("exited")
   break
  else:
    print("sorry...I do not understand...Try again");

    

    
    