"""class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        res = 0
        for i in range(len(s)-1):
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == '0' and s[right] == '1':
                res += 1
                left -= 1
                right += 1
        for i in range(len(s)-1):
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == '1' and s[right] == '0':
                res += 1
                left -= 1
                right += 1
        return res
        """
        """
        res = 0
        snum_list = []
        index = 0
        cnt = 1
        while index < len(s) - 1:
            if s[index] == s[index + 1]:
                cnt += 1
                index += 1
            else:
                snum_list.append(cnt)
                cnt = 1
                index += 1
        snum_list.append(cnt)
        for i in range(len(snum_list) - 1):
            res += min(snum_list[i], snum_list[i + 1])
        return res
        """
        res = 0
        snum_list = [1]
        tmp = 0
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                snum_list.append(1)
                tmp += 1
            else:
                snum_list[tmp] += 1
        for i in range(len(snum_list) - 1):
            res += min(snum_list[i], snum_list[i + 1])
        return res
        
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
"""

