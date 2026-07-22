class Solution:
    #
    # Because it mentions that nums1 and nums2 are unique, it suggests to me that we can use the values as some key to a hash (dictionary)
    # What we can actually do, is basically, we can find all the next greater elements in nums2, then after we have the mapping
    # We can make a list using the values in num1 as keys, since all values in num1 are in num2 (definition of subset)
    # Then what we can do, is if they don't have a greater element, we have the value as -1
    # The approach I am thinking of taking is a monotonic stack, it will allow us to preserve order
    # We will have the stack in decreasing order, from bottom to top
    # We will iterate like so, while element at top < value x
    # Pop it
    # Otherwise append/push value x onto the stack, allows us to preserve order, and means that, we haven't found the next greatest element for the element at the top of stack yet.
    # This way, the element that gets popped by some value x, next_greater[popped_element] = value x
    #
    # Total runtime for this is O(n + m)
    # We have O(m) 2m for pop and push operations where n is len(nums2)
    # We have O(n) hashes for final array, where m is len(nums1)
    # Space Complexity O(n)
    # The dictionary contains at most n keys
    # The array contains at most n values, since nums1 is subset of nums2, worst case len(nums1) = len(nums2)
    # Hence O(n) + O(n) = O(n)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for index, value in enumerate(nums2):
            while stack and stack[-1] < value:
                j = stack.pop()
                next_greater[j] = value
            stack.append(value)
        return [next_greater.get(value, -1) for value in nums1]
        # This will get the values from nums1 check their keys inside next_greater, if the key doesn't exist, then we return -1