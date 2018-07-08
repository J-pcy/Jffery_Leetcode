"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #return str(int(num1) * int(num2))
        """
        number1 = 0
        number2 = 0
        res = []
        for i in num1:
            number1 = number1 * 10 + (ord(i) - ord('0'))
        for i in num2:
            number2 = number2 * 10 + (ord(i) - ord('0'))
        product = number1 * number2
        if product == 0:
            return '0'
        while product:
            res.append(str(product % 10))
            product //= 10
        res.reverse()
        return ''.join(res)
        """
        """
        carry = 0
        len1, len2 = len(num1), len(num2)
        product = [0] * (len1 + len2)
        for i in range(len1):
            for j in range(len2):
                product[len1 + len2 - 2 - i - j] += (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
        for i in range(len(product)):
            product[i] += carry
            carry = product[i] // 10
            product[i] %= 10
        i = len1 + len2 - 1
        while product[i] == 0:
            product.pop()
            i -= 1
            if i < 0:
                return '0'
        while i >= 0:
            product[i] = str(product[i])
            i -= 1
        product.reverse()
        return ''.join(product)
        """
        if len(num1) == 0 or len(num2) == 0:
            return ''
        if num1 == '0' or num2 == '0':
            return '0'
        num = 0
        res = []
        for i in range(len(num1) + len(num2), -1, -1):
            j = min(i - 1, len(num1))
            while j > 0:
                if i - j <= len(num2):
                    num += (ord(num1[j - 1]) - ord('0')) * (ord(num2[i - 1 - j]) - ord('0'))
                j -= 1
            if i > 1 or num > 0:
                res.append(str(num % 10))
                num //= 10
        res.reverse()
        return ''.join(res)
        