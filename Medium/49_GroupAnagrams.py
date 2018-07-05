"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """
        #exceed time limit
        res = []
        while strs:
            tmp = [strs[0]]
            i = 1
            while i < len(strs):
                if self.isAnagrams(strs[0], strs[i]):
                    tmp.append(strs[i])
                    strs.pop(i)
                else:
                    i += 1
            res.append(tmp)
            strs.pop(0)
        return res
    
    def isAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        sdict = {}
        for i in s1:
            sdict[i] = sdict.get(i, 0) + 1
        for i in s2:
            if i not in sdict:
                return False
            else:
                if sdict[i] <= 0:
                    return False
                sdict[i] -= 1
        return True
        """
        #res = []
        sdict = {}
        for i in range(len(strs)):
            tmplist = list(strs[i])
            tmplist.sort()
            tmp = ''.join(tmplist)
            if tmp not in sdict:
                sdict[tmp] = [strs[i]]
            else:
                sdict[tmp].append(strs[i])
        #for i in sdict.values():
            #res.append(i)
        return list(sdict.values())
        