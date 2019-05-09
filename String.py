a=input("enter string :")
revstring=""
for i in a:
  revstring=i+revstring
if revstring==a:
  print("string is palindrome")
else:
  print("string is not palindrome")