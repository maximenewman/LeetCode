class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        We don't want duplicates, so the best datastructure for this is a set
        We add our values to the set
        Then we check if the value is already in the set
        A set has O(1) -> Lookup
        If it is, then we return True -> has duplicate

        If not we keep appending, till we exit the loop, or hit a duplicate

        Time complexity -> O(n)
        We iterate through the array once, Each lookup and insertion is O(1) on average,
        hence our overall time complexity is the in the worst case is the input size -> O(n)
				
        Space Complexity -> O(n)
        In the worst case we create a set of size n, where there are no duplicates
        """
        seen = set()
        for num in nums:
            if(num in seen):
                return True
            else:
                seen.add(num)
        return False