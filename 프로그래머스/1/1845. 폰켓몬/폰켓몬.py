def solution(nums):
    h_dict = dict()
    
    for i in nums:
        h_dict[i] = 1
        
    if len(nums) // 2 <= len(h_dict):
        return len(nums)//2
    return len(h_dict)