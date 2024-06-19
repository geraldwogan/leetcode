class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s)==1:
            return s
        best = s[0]
        # print(s[::-1][0])
        # print(s[1::-3])
        for i, ival in enumerate(s):
            for j, jval in enumerate(s):
                if j+1-i>len(best):
                # print(f'index[{i}] -> index[{j+1}]')
                # print(f'{s[i:j+1]} vs {s[i:j+1][::-1]}')

                    if s[i:j+1] == (s[i:j+1][::-1]):
                    #     # print(s[i:j+1])
                        best = s[i:j+1]
        
        return best
                