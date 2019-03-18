from datetime import datetime
def Age(DOB):
    currenttime=datetime.now()
    Age=(currenttime.year)-(DOB.year)
    
    if(Age>0):
        print("Your age is "+str(Age)+" year(s)")
    else :
        print("Year should be between 1969 and 2018. Please try again")
    return
UserIn=input("Enter your DOB in the format DD/MM/YY: ")
isValidDate = True
try :
    day,month,year = UserIn.split('/')
    datetime(int(year),int(month),int(day))
except ValueError :
    isValidDate = False
if(isValidDate) :
    try :
        DOB = datetime.strptime(UserIn,"%d/%m/%y")
        Age(DOB)
    except ValueError :
        print("Invalid date format. Please enter 2 digit year and try again")
        exit()
else :
    print ("Input date is either blank or not valid. Please try again")

#test cases
# User should not be able to enter negative numbers. It's output is coming as negative float
# User Cannot have year restritions. this could be achieved by changing the year format to 4 digit
