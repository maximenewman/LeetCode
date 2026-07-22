class Solution:
    # s is a string, that contains different parentheses "(),[],{}"
    # To be Valid:
    # 1. Open brackets closed by the same type of bracket
    # Example 5, shows us that
    # if we have an open bracket, the next thing possible is either another open bracket, or the same closing bracket
    # 2. Open brackets must be closed in the correct order
    # Example 5
    # If you have an open bracket, the next closing bracket, must be of the same type
    # "([)]"
    # The next closing bracket should have been ]
    # 3. Every closing bracket has a corresponding oepn bracket of the same type
    # )], somewhere in the string you need to have the same openning bracket
    # Also, based on rule 2, a closing bracket, can never come before one of it's open brackets
    # Why? Essentially because that would mean they were closed in the wrong order
    #
    # My Approach is to use a stack
    # Why should I use a stack, because we want to keep track of the last character that we saw
    # Given a string for instance
    # "([)]"
    # We will append only the openning brackets
    # What I mean is that, openning brackets can compound like so ([{
    # But as soon as we touch a closing bracket, it must be the same as the openning bracket.
    # So we need to know what openning bracket was last
    # So actually we can make a dictionary of pairs, with closing brackets as the key, and the openning brackets as the #values. Then we iterate through the string
    # "([)]"
    # add the oppening brackets to the stack when we see them
    # Check if we see a closing bracket, if we do, and the top of the stack isn't the same openning bracket, then return 
    # false immediately.
    # Otherwise pop, and continue.
    # Run time 
    # Iterate through the string O(n)
    # Check for closing (in operator for set/dict O(1))
    # Time complexity O(n)
    # Space Complexity O(m)
    # Setting up pairs -> O(1), always going to be the same size
    # Stack is going to be O(m), where m is the number of open brackets
    # 
    def isValid(self, s: str) -> bool:
        #define the pairs
        pairs = {"]": "[", ")": "(", "}": "{"}
        #define the stack
        stack = []
        for char in s:
            # Check if it is a closing bracket
            if char in pairs:
                #If the closing bracket ever appears before an openning then false
                if not stack or stack.pop() != pairs[char]:
                    return False
                # if it is the same, we already popped it so we can continue to check the next element do nothing
            else:
                #if it is an openning bracket, they can stack so just append
                stack.append(char)
        #At the end, if we have a valid string, the stack should be empty
        return not stack
        #If it is empty -> true
        #If it is not empty -> invalid -> false
        