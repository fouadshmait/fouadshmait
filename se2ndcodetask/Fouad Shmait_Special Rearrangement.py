def  special_rearrangement(nums):
 odd_numbers = [] 
 even_numbers = []
 
 for i in range(len(nums)):
    if nums[i] % 2 == 0:
      even_numbers.append(nums[i])
    else:
      odd_numbers.append(nums[i])
      
 arrange_nums = even_numbers + odd_numbers

 return arrange_nums
number=[5,4,1,7,8,9]
print(special_rearrangement(number))
       
   
          
   
      
     


