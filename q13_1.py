class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanToInt = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # traverse through s using i:
        # -> if i + 1 < len(s) && romanToInt[s[i]] < romanToInt[s[i + 1]]:
        #       res += romanToInt[s[i + 1]] - romanToInt[s[i]]
        #       i++
        # -> else:
        #       res += romanToInt[s[i]]
        # return res

        res, i = 0, 0
        while i < len(s):
            if i + 1 < len(s) and romanToInt[s[i]] < romanToInt[s[i + 1]]:
                res += romanToInt[s[i + 1]] - romanToInt[s[i]]
                i += 2
            else:
                res += romanToInt[s[i]]
                i += 1
        
        return res
