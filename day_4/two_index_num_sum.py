def twosum(nums:list[int], target:int) -> int:
        
     for i in range(len(nums)):
        for j in range(i+1, len(nums)):
                
            if nums[i] +nums[j] == target:
                 return[i,j]
               
nums = [6,5,7,3,4]
target = 7

result = twosum(nums, target)

print(result)