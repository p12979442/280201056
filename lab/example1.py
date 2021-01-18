numbers=[43,342,343,2,34]
def selection_sort(num):
  if len(num)==1:
    return num
  maxi=num[0]
  for i in num:
    if maxi>i:
      maxi=i
  num.remove(maxi)
  num.append(maxi)    
  return [maxi]+ selection_sort(num[:len(num)-1])
print(selection_sort(numbers))