def move_zeros(numbers):
 for i in range(len(numbers)):
   if numbers[i]==0:
     for j in range(i+1,len(numbers)):
      if numbers[j] != 0:
        numbers[i],numbers[j]=numbers[j],numbers[i]
        
 return numbers
numbers = [1,10,0,2,0,9,6,4]
print(move_zeros(numbers))
        
     
