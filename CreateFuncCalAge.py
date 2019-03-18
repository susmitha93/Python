from datetime import datetime
def Age(DOB):
    currenttime=datetime.now()
    Age=(currenttime.year)-(DOB.year)
    if(Age>0):
        print("Your age is "+str(Age))
    else :
        print("You have either entered a future date or too old date to calculate. Please try again")
    return
UserIn=input("Enter your DOB in the format DD/MM/YYYY: ")
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
    print ("Input date is either blank or not valid format. Please enter date in DD/MM/YY format and try again")