n = int(input("Enter an interger : "))
print("You entered :",n)
L = []
for _ in range(n) :
  num = int(input("Enter an interger :"))
  L.append(num)
  print("Append :",L)
  max_element = max(L)
  min_element = min(L)
  print("Maximum element : ",max_element)
  print("Min element : ", min_element)
  #Compute the sum of element
  sum_element = sum(L)
  print("Sum of element in L : " ,sum_element)
  sort_list = L.sort()
  print(" Sort the list L in ascending order : ",sort_list)
  # Show how many positive and negative numbers are in the list L.
  pos_count = 0
  neg_count = 0
  for num in L :
    if num > 0 :
      pos_count += 1
    if num < 0 :
      neg_count += 1
      print("Number of positive numbers:", pos_count)
      print("Number of negative numbers:" , neg_count)
