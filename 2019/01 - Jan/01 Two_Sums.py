class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # Soln 1
        # @time = 1520 ms
        for i in range(len(nums) - 1):
            cur = nums[i]
            rest_nums = nums[i+1:]
            rest_target = target - cur
            if rest_target in rest_nums:
                second_index = rest_nums.index(rest_target) + (i+1)
                return [i, second_index]



        # Soln 2
        # @time = 84 ms
        # @complexity O(n) - fastest
        prev_nums = {}
        for i in range(len(nums)):
            cur = nums[i]
            rest = target - cur
            if rest in prev_nums:
                return [prev_nums[rest], i]
            else:
                prev_nums[cur] = i