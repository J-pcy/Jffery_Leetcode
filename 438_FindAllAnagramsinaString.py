"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        """
        slist = [0] * 128
        plist = [0] * 128
        plen = len(p)
        res = []
        if len(s) == 0 or len(s) < plen:
            return res
        for i in range(plen):
            slist[ord(s[i])] += 1
            plist[ord(p[i])] += 1
        if slist == plist:
            res.append(0)
        for i in range(plen, len(s)):
            slist[ord(s[i])] += 1
            slist[ord(s[i - plen])] -= 1
            if slist == plist:
                res.append(i - plen + 1)
        return res
        """
        res = []
        cnt = len(p)
        left = right = 0
        pdict = {}
        for i in p:
            pdict[i] = pdict.get(i, 0) + 1
        while right < len(s):
            if s[right] in pdict:
                if pdict[s[right]] > 0:
                    cnt -= 1
                pdict[s[right]] -= 1
            right += 1
            if cnt == 0:
                res.append(left)
            if right - left == len(p):
                if s[left] in pdict:
                    if pdict[s[left]] >= 0:
                        cnt += 1
                    pdict[s[left]] += 1
                left += 1
        return res
        