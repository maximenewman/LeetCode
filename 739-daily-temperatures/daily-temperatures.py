class Solution:
    # Array of integers -> Temps
    # Return array of answers, that tells us, for an index i, for value temp[i] what is the number of days you have to wait
    # after the ith day to get a warmer temperature. That value will be answers[i]
    #
    # We need to keep track of the current temperature, and then we need to find the first temperature that is warmer
    # A brute force approach, is to iterate each temperature individually
    # That is we have two loops
    # One that starts at the beginning of the array index i
    # and the other starts at index i + 1 = j
    # Then when we find a value such that temp[i] < temp[j]
    # Then we do we append the value j - i into the answers array
    # If there is no value greater than it, we return 0
    # We stop at value j = len(temp) - 1
    #
    """
    def dailyTemperatures(self, temperatures: List[int])-> List[int]:
        n = len(temperatures)
        answers: List = [0] * n
        for i in range(n):
            for j in range(i+1, n):
                print(f"i: {i}, j: {j}, temp[i] = {temperatures[i]}, temp[j] = {temperatures[j]}")
                if temperatures[i] < temperatures[j]:
                    answers[i] = (j-i)
                    break
        return answers
    """ 
    # Time Complexity O(n^2)
    # Space Complexity O(n)
    # A more optimal solution is to use a monotonic stack, in order to find the next greatest element
    # Basically, the intuition is that for a given temperature, we are only concerned with the first occurence of greater than the current value
    # So what we can do is maintain a decreasing stack
    # Pop all the values less than or equal the current value being compared
    # Then if we reach a value that is greater than the current value being compared
    # The previous value that was at the top, its next greatest value is the value being compared.
    # We keep track of the indices inside the stack
    # The runtime for this algorithm is going to be O(n)
    # Why?
    # Essentially, each index is pushed once and popped at most once. No index is reintroduced. So Max 2n operations -> O(n)
    # The invariant is what makes the popped answers right. When x pops index j, you're claiming x is temp[j's] nearest greater element to the right. That claim depends on nothing between j and x having beaten j. And the reason you can trust that is that anything that beat j would have popped it already. j still being on the stack is a proof that nothing in between qualified.
    # Space Complexity O(n), worst case, temperatures are in decreasing order, stack grows to size of len(temperatures)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n: int = len(temperatures)
        res: List[int] = [0] * n
        stack = []
        for index, value in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < value:
                # we store the indexes inside the stack
                j = stack.pop()
                # whatever we pop, it's next greatest element is the value being compared
                res[j] = index - j
                # This indicates the distance between the days
            stack.append(index)
        return res