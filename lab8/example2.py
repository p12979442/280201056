def prime(x):
  counter=0
  for i in range(1,x+1):
    if x%i==0:
      counter+=1
    else:
      counter+=0
  if counter==2:
    print(x,"is prime")
  else:
    print(x,"isn't prime")
  prime_list=[]
  for i in range(1,x+1):
    counter2=0
    for n in range(1,i+1):
      if i%n==0:
        counter2+=1
    if counter2==2:
      prime_list.append(i)

  for i in prime_list:
    if i==5:
      break
    print(i,"is prime")
    
prime(5)