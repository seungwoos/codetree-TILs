import sys

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = -sys.maxsize

def get_rectangle_sum(x1, y1, x2, y2):
    if 0 <= x1 < n and 0 <= y1 < m and 0 <= x2 < n and 0 <= y2 < m:
        if x1 == x2 and y1 == y2:
            return grid[x1][y1]

        return sum([
            grid[i][j]
            for i in range(x1, x2+1)
            for j in range(y1, y2+1)
        ])
    else:
        return -sys.maxsize

for i in range(n):
    for j in range(m):

        for height_1 in range(n):
            for width_1 in range(m):
                area_1 = get_rectangle_sum(i, j, i+height_1, j+width_1)

                for x in range(n):
                    for y in range(m):

                        for height_2 in range(n):
                            for width_2 in range(m):
                                if x <= i + height_1 and y <= j + width_1:
                                    continue

                                area_2 = get_rectangle_sum(x, y, x+height_2, y+width_2)

                                answer = max(answer, area_1 + area_2)
print(answer)