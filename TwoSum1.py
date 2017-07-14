class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for x in range(len(nums)):
            left = target - nums[x]
            if nums[x] not in map.keys():
                map[left] = x
            else:
                return [map[nums[x]],x]

