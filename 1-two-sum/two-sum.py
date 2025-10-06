class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        We want to find the target, and store the indices that sum to it
        To do this, we will create a new array to store our indeces
        Since the question, specifies that there is only 1 pair of indices
        we can imediately return, once we find the matching indices
        [3,4,5,6]
        """

        new_map: dict = {}
        # high: int = len(nums) - 1
        """
        Since we are always incrementing
        Then we are only searching for values that are already in the list
        Hence we know that the new values index will always be greater than the old values
        That we are checking for
        """
        for i in range(len(nums)):
            if (target - nums[i]) in new_map:
                return [new_map[target-nums[i]], i]
            if nums[i] not in new_map:
                new_map[nums[i]] = i

        print(new_map)
        return []