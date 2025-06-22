N, Q = map(int, input().split())
cells = [0 for _ in range(N)]
ans = 0
A = [*map(int, input().split())]

def is_both_ends_color(i, color):
    # 0-indexed
    ans = True
    global cells
    global N
    if i-1>=0:
        if cells[i-1] != color:
            ans = False
    if i+1<N:
        if cells[i+1] != color:
            ans = False
    return ans

for a in A:
    # print(cells)
    if cells[a-1] == 0:
        # 白→黒の場合
        cells[a-1] = 1
        if a-2>=0 and a<N:
            # 両端が白の場合ans+=1
            if is_both_ends_color(a-1, 0):
                # print('a')
                ans += 1
            # 両端が黒の場合ans-=1
            if is_both_ends_color(a-1, 1):
                # print('b')
                ans -= 1
        else:
            if a<N:
                if cells[a] == 0:
                    # print('c')
                    ans += 1
            if a-2>=0:
                if cells[a-2] == 0:
                    # print('d')
                    ans += 1
            if a>=N and a-2<0:
                ans += 1
    else:
        # 黒→白の場合
        cells[a-1] = 0
        if a-2>=0 and a<N:
            # 両端が白の場合ans-=1
            if is_both_ends_color(a-1, 0):
                # print('e')
                ans -= 1
            # 両端が黒の場合ans++=1
            if is_both_ends_color(a-1, 1):
                # print('f')
                ans += 1
        else:
            if a<N:
                if cells[a] == 0:
                    # print('g')
                    ans -= 1
            if a-2>=0:
                if cells[a-2] == 0:
                    # print('h')
                    ans -= 1
            if a>=N and a-2<0:
                ans -= 1
    print(ans)
    
    