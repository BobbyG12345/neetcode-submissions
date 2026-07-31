class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_set = set()
        longest = 0
        current_long = 0
        left = 0

        for right in range(len(s)):
            while s[right] in c_set:
                c_set.remove(s[left])
                left += 1
                current_long -= 1

            c_set.add(s[right])
            current_long += 1
            longest = max(longest, current_long)

        return longest
