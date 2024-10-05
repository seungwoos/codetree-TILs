import copy

n, m, q = map(int, input().split())
building = [list(map(int, input().split())) for _ in range(n)]

def clockwise_shift(r1, c1, r2, c2):
    tmp = building[r1][c1]

    for i in range(r1, r2):
        building[i][c1] = building[i+1][c1]
    
    for i in range(c1, c2):
        building[r2][i] = building[r2][i+1]
    
    for i in range(r2, r1, -1):
        building[i][c2] = building[i-1][c2]
    
    for i in range(c2, c1, -1):
        building[r1][i] = building[r1][i-1]
    
    building[r1][c1+1] = tmp

def average_nearest(r1, c1, r2, c2):
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    tmp = copy.deepcopy(building)
    
    for i in range(r1, r2):
        for j in range(c1, c2):
            local_sum = building[i][j]
            cnt = 1
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m:
                    local_sum += building[nx][ny]
                    cnt += 1
            
            tmp[i][j] = local_sum // cnt
    
    return tmp

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())

    clockwise_shift(r1-1, c1-1, r2-1, c2-1)
    building = average_nearest(r1-1, c1-1, r2, c2)

for i in range(n):
    print(*building[i])