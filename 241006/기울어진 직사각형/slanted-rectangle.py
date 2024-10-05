n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0

dx = [-1, -1, 1, 1]
dy = [1, -1, -1, 1]

def check_in_range(i, j):
    return 0 <= i < n and 0 <= j < n

def get_triangle_sum(i, j, r_k, c_k):
    triangle_sum = 0

    for _ in range(r_k):
        i, j = i + dx[0], j + dy[0]
        if check_in_range(i, j):
            triangle_sum += grid[i][j]
        else:
            return 0

    for _ in range(c_k):
        i, j = i + dx[1], j + dy[1]
        if check_in_range(i, j):
            triangle_sum += grid[i][j]
        else:
            return 0

    for _ in range(r_k):
        i, j = i + dx[2], j + dy[2]
        if check_in_range(i, j):
            triangle_sum += grid[i][j]
        else:
            return 0

    for _ in range(c_k):
        i, j = i + dx[3], j + dy[3]
        if check_in_range(i, j):
            triangle_sum += grid[i][j]
        else:
            return 0

    return triangle_sum

for i in range(n):
    for j in range(n):
        for r_k in range(1, n):
            for c_k in range(1, n):
                triangle_sum = get_triangle_sum(i, j, r_k, c_k)
                answer = max(answer, triangle_sum)

print(answer)