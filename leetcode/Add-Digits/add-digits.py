class Solution:
    def addDigits(self, num: int) -> int:
        string = str(num)
        res = num
        while len(string) > 1:
            y = 0
            for x in string:
                y += int(x)
            res = y
            string = str(res)
        return res

x = Solution().addDigits
print(x(38))