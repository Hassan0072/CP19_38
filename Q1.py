sen1=input("Enter 1st sentence = ")
sen2=input("Enter 2nd sentence = ")
sen1=sen1.split(" ")
sen2=sen2.split(" ")
print("Ahsan")
print("Karachi")
print("Pakistan")
x=1
for i in range(len(sen1)):
    for j in range(len(sen2)):
        if sen1[i]==sen2[j]:
            
            print("common word ",x," : ",sen1[i])
            x+=1