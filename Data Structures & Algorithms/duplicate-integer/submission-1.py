class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        i = 0
        n = len(nums)

        while i<n:
            num = nums[i]
            if num in seen:
                return True
            seen.add(num)
            i+=1
        return False

        
        