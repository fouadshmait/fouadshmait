
fib = int(input(" please enter a number : "))
sum_list=[0,1]
  
for i in range(1,fib):
  next=sum_list[i-1]+sum_list[i]
  sum_list.append(next)
  print(sum_list)

