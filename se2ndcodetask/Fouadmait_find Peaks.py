def find_peaks(array):
  counter = [] 
  for i in range (1,len(array)-1):
    if array[i] > array[i-1] and array[i]>array[i+1]:
      counter.append(i)
  return counter
array=[1,4,3,7,8,2]
print(find_peaks(array))
