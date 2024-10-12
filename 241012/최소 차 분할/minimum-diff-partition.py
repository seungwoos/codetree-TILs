import sys

n = int(input())
nums = list(map(int, input().split()))

total = sum(nums)

dp = [False for _ in range(total + 1)]

dp[nums[0]] = True

for i in range(1, n):
    num = nums[i]
    tmp = []

    for j in range(total):
        if dp[j]:
            dp[j] = False

            # 1. Same group
            tmp.append(j + num)
            # 2. different
            tmp.append(abs(j - num))
        
    for n in tmp:
        dp[n] = True

for i in range(total + 1):
    if dp[i]:
        print(i)
        break