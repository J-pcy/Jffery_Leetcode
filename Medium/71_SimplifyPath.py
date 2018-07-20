"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""

class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        """
        paths = path.split('/')
        res = '/'
        index = 0
        while index < len(paths):
            if paths[index] == '.' or paths[index] == '':
                paths.pop(index)
            elif paths[index] == '..':
                paths.pop(index)
                if index > 0:
                    paths.pop(index - 1)
                    index -= 1
            else:
                index += 1
        for i in range(len(paths)):
            res += '/' + paths[i] if res != '/' else paths[i]
        return res
        """
        res = path.split('/')
        index = 0
        while index < len(res):
            if res[index] == '.' or res[index] == '':
                res.pop(index)
            elif res[index] == '..':
                res.pop(index)
                if index > 0:
                    res.pop(index - 1)
                    index -= 1
            else:
                index += 1
        return '/' + '/'.join(res)
        