class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        We want to repeat the array 2 times -> resulting in an array of size 2n
        ans[i] == nums[i]
        ans[i + n] = nums[i] -> This means we loop back on the array, once we have iterated n times
        This can also be rewritten as ans[i] = nums[i - n] -> Where i is an index that is increasing
        If we loop once, then ans[i] = nums[i - n]
        if we loop twice, then ans[i] = nums[i - 2n]
        if we loop three times, then ans[i] = nums[i - 3n] and so forth. Hence we have a pattern.
        Every j loops, we subtract our index by j*n. Where n is the array size.
        To know if we are on to the next loop, the mod of i and n should be 0. 
        Example:
        We loop once. i == n: i % n == 0
        We loop twice. i == 2n: i % n == 0 -> 2n / n = 1 remainder 0
        and so forth
        This is how we will increment j

    With this, we can find a better approach

    ans[i] = nums[i % n] -> There will always be n remainders
    from 0 -> n-1, which is exactly the indexes we want


    Since we are iterating through the array 2 times our time complexity is
        O(2 * n) -> O(n)
        In general it is O(m * n), where m is the number of times we iterate through the array
        The space complexity is O(n), since we ans will grow with input
        Hence if input is 2n ans = 4n
        """
        x: int = 2
        ans: List[int] = []
        for i in range(len(nums) * x):
            ans.append(nums[i % len(nums)])

        return ans
        