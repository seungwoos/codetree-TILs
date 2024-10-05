n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

r, c, m1, m2, m3, m4, direction = map(int, input().split())

r, c = r-1, c-1

def move_left_up(r, c, m):
    for _ in range(m):
        grid[r][c] = grid[r+1][c+1]
        r, c = r+1, c+1

    return r, c

def move_right_up(r, c, m):
    for _ in range(m):
        grid[r][c] = grid[r+1][c-1]
        r, c = r+1, c-1

    return r, c

def move_left_down(r, c, m):
    for _ in range(m):
        grid[r][c] = grid[r-1][c+1]
        r, c = r-1, c+1

    return r, c

def move_right_down(r, c, m):
    for _ in range(m):
        grid[r][c] = grid[r-1][c-1]
        r, c = r-1, c-1

    return r, c

if direction == 0:
    tmp = grid[r][c]
    r, c = move_right_down(r, c, m4)
    r, c = move_left_down(r, c, m3)
    r, c = move_left_up(r, c, m2)
    r, c = move_right_up(r, c, m1)

    grid[r-1][c+1] = tmp
    
else:
    tmp = grid[r][c]
    r, c = move_left_down(r, c, m1)
    r, c = move_right_down(r, c, m2)
    r, c = move_right_up(r, c, m3)
    r, c = move_left_up(r, c, m4)

    grid[r-1][c-1] = tmp

for i in range(n):
    print(*grid[i])