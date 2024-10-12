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

            tmp.append(abs(j - num))
            tmp.append(j + num)
    
    for n in tmp:
        dp[n] = True

if dp[0]:
    print("Yes")
else:
    print("No")