def maxSubArray(nums):
    max_sub=nums[0]
    current_sum=0
    for n in nums:
        if current_Sum<0:
            current sum=0
        current_sum+=n
        max_sub=max(max_sub,current_sum)
    return max_sub    
