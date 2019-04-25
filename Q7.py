import datetime
date=datetime.datetime.now()

day=date.day
m=date.month
y=date.year
currentdate=str(day)+"/"+str(m)+"/"+str(y)
currentdate2=currentdate.split("/")

d=input("Enter Date in Format dd/mm/yyyy : ")
d1=d.split("/")
if(d1[2]==currentdate2[2]):
    
    
    if(d1[1]==currentdate2[1]):
        
        
        if(d1[0]==currentdate2[0]):
            print("Date is Same :",d,"==",currentdate)
        elif(int(d1[0])<int(currentdate2[0])):
            print("Input  Date is Less from current Date :",d,"<",currentdate)
        else:
            print("Input  Date is Greater from current Date :",d,">",currentdate)
            
            
            
    elif(int(d1[1])<int(currentdate2[1])):
       
        print("Input  Date is less from current Date :",d,"<",currentdate)
    elif(int(d1[1])>int(currentdate2[1])):
        print("Input  Date is Greater from current Date :",d,">",currentdate)
        
        
        
elif(int(d1[2])<int(currentdate2[2])):
    print("Input  Date is Less from current Date :",d,"<",currentdate)
else:
    print("Input  Date is Greater from current Date :",d,">",currentdate)
  