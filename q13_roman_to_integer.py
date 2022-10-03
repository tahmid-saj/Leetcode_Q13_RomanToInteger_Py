class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        i = 0
        rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        while i < len(s):
            if i != len(s) - 1 and rom_num[s[i]] < rom_num[s[i + 1]]:
                num += rom_num[s[i + 1]] - rom_num[s[i]]
                i += 1
            else:
                num += rom_num[s[i]]
            i += 1
        
        return num
        