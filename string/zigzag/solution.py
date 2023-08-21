class ZigZag:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = [""] * numRows
        i = 0
        opr = 1
        for c in s:
            ans[i] += c
            if i == 0:
                opr = 1
            if i == (numRows-1):
                opr = -1
            i += opr
        return "".join(ans)