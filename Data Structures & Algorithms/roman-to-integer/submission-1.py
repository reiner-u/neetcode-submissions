class Solution:
    def romanToInt(self, s: str) -> int:
        romanInt = {'M': 1000, 'CM':900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        num = 0
        for i in range(len(s)-1):
            if romanInt[s[i]]<romanInt[s[i+1]]:
                num-=romanInt[s[i]]
            else: 
                num+=romanInt[s[i]]
        num+=romanInt[s[len(s)-1]]
        return num