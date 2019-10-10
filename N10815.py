def binary_search(num):
    left = 0
    right = n-1
    while left <= right :
        mid = (left+right)//2
        if intCard[mid] == num :
            return 1
        elif intCard[mid] > num :
            right = mid - 1
            # 반 줄여주기 1
        else:
            left = mid + 1
            # 반 줄여주기 2
    return 0

n = int(input())
intCard = list(map(int, input().split()))
intCard.sort()

input() #M
for num in list(map(int, input().split())):
    print(binary_search(num), end = ' ')