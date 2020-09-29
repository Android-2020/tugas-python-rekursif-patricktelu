def rekursif(i):
  print(i, end="")
  if i >=0:
    i = i-1
    rekursif(i)
    
rekursif(5)
