num = int(input("enter number:"))
def pyrmid(num):
  value = 1
  for i in range(1,num+1):

    for j in range(i,num):
      print(" ",end=" ")

    for j in range(0,value):
        if (j%2 == 0):
          print("4",end=" ")
        else:
          print("1",end=" ")
    print()
    value = value + 2

pyrmid(num)