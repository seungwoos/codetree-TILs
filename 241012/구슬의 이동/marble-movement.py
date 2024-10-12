import sys
import copy

input = sys.stdin.readline

n, m, t, k = map(int, input().split())
grid = [[[] for _ in range(n)] for _ in range(n)]
beads = [[0]]

dir2int = {
    "L": 0,
    "U": 1,
    "R": 2,
    "D": 3,
}

dxs = [0, -1, 0, 1]
dys = [-1, 0, 1, 0]

def initialize():
    for i in range(m):
        r, c, d, v = map(str, input().split())
        r, c, v = int(r) -1 , int(c) - 1, int(v)

        grid[r][c].append(i + 1)
        beads.append([dir2int[d], v])

def check_in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def simulate():
    global grid

    tmp = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):

            if len(grid[i][j]) > 0:
                for bead_id in grid[i][j]:
                    d, v = beads[bead_id]
                    x, y = i, j

                    for _ in range(v):
                        nx, ny = x + dxs[d], y + dys[d]

                        if not check_in_range(nx, ny):
                            nx, ny = x, y
                            d = (d + 2) % 4
                            beads[bead_id][0] = d

                            nx, ny = x + dxs[d], y + dys[d]

                        x, y = nx, ny

                    tmp[x][y].append(bead_id)
    
    for i in range(n):
        for j in range(n):

            if len(tmp[i][j]) > k:
                ids = copy.deepcopy(tmp[i][j])
                vels = [beads[id][1] for id in ids]
                
                vels, ids = zip(*sorted(list(zip(vels, ids)), reverse=True))

                tmp[i][j] = list(ids)[:k]                

    grid = copy.deepcopy(tmp)

if __name__ == "__main__":
    initialize()

    for _ in range(t):
        simulate()
    
    answer = 0
    for i in range(n):
        for j in range(n):
            answer += len(grid[i][j])
    
    print(answer)