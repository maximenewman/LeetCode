class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
				To determine if two strings are anagrams, we count how many times each
				character appears in the first string using a hashmap (dictionary).
				Then, as we scan the second string, we decrement the corresponding counts.

				If:
				- we ever see a character not in the dictionary, or
				- a count drops below zero,

				then the strings are not anagrams.

				After processing all characters, if all counts return to zero,
				the strings contain exactly the same characters in the same quantities.
        
        Time complexity: O(n)
        We iterate through string and map each letters count to each letter
        O(1) -> For each key created on average
        O(1) -> condition check
        O(1) -> increment
        
        Then we check that the letters are in the dictionary
        O(1) -> lookup
        O(1) -> decrement
        
        Total of O(n)
        
        Space Complexity: O(n)
        We create a dictionary of the same size as the number of distinct letters
        Worst case the whole string contains no duplicates
        Hence we have space complexity of O(n)
        """
        if(len(s) != len(t)):
            return False

        letters: dict = {}
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

        for letter in t:
            if letter not in letters:
                return False
            else:
	            letters[letter] -= 1
            if letters[letter] < 0:
                return False

        return True
