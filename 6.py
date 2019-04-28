def prime(value):
    if(value>0):
        i=1
        count=0
        result=0
        while(i<=value):
            result=value%i
            
            if(result==0):
                count+=1
            i+=1
        if(count==2):
            print(value," is a Prime No")
        
        else:
            print(value," Is Not Prime No")
value=int(input("Enter A No : "))
prime(value)