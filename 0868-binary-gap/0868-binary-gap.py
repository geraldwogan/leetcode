class Solution:
    def binaryGap(self, n: int) -> int:
        # Delete all non 0/1 values
        valids = [x for x in bin(n) if x=='0' or x=='1']

        # Return lists of binary gaps
        # Delete start and end list, as they are not 'gaps'
        valids = ''.join(valids).split('1')[1:-1]

        # Get len for all valids binary gaps
        b = [len(x)+1 for x in valids]

        # Return largest binary gap, if none exists, return 0
        return max(b) if len(b)>0 else 0
