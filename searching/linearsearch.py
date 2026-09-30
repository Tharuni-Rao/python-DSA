def linearsearch(a,el):
  ar=[]
  for i in range(len(a)):
    if a[i] == el:
      ar.append(i)


  if len(ar)>0:        
    return ar
  return -1  



a=[1,31,12,9,18,2,12,12]
print(linearsearch(a,12))