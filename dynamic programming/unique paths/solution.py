class Solution:
    # Top-down approach
    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[0]*n]*m
        for i in range(m):
            for j in range(n):
                if (j == 0) or (i == 0):
                    mat[i][j] = 1
                else:
                    mat[i][j] = mat[i-1][j] + mat[i][j-1]
        return mat[m-1][n-1]

    # Bottom-up approach
    def travel(self, m: int, n: int) -> int:
        if self.route[m-1][n-1] > 0:
            return self.route[m-1][n-1]
        elif m == 1 and n == 1:
            self.route[0][0] = 1
        elif m == 1:
            self.route[0][n-1] = self.travel(1, n-1)
        elif n == 1:
            self.route[m-1][0] = self.travel(m-1, 1)
        else:
            self.route[m-1][n-1] = self.travel(m-1, n) + self.travel(m, n-1)
        return self.route[m-1][n-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        self.route = [[0]*n for _ in range(m)]
        return self.travel(m, n)
