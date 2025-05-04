# 回転回数を全探索

N = int(input())
S = [[*input()] for i in range(N)]
T = [[*input()] for i in range(N)]

def rotate(grid):
    ans = [["" for j in range(N)] for i in range(N)]
    for Y in range(N):
        for X in range(N):
            ans[Y][N-X-1] = grid[X][Y]
    return ans
            
def count_not_match_cells(S, T):
    ans = 0
    for j in range(N):
        for i in range(N):
            if S[i][j] != T[i][j]:
                ans += 1
    return ans
    
ans = list()
ans.append(count_not_match_cells(S, T))

for i in range(1, 4):
    S = rotate(S)
    ans.append(count_not_match_cells(S, T)+i)
    
print(min(ans))