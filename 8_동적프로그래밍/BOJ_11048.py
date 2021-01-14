'''
    문제설명
        백준 11048 이동하기 (DP 이용)
        미로 (1,1)에서 (n,m)으로 이동할 때 가져올 수 있는 사탕의 최댓값 구하기
    해결전략
        다이나믹 프로그래밍 이용한다. 작은 문제로 쪼개고 해를 찾은 후 그 해를 바탕으로 더 큰 문제의 해를 구한다.
        dy[i][j]는 (0,0)에서 (i,j)까지 가는데 가져올 수 있는 사탕의 최댓값을 의미한다.
        원래는 10, 12, 9시 세 방향에서 이동할 수 있지만 dy의 0행과 0열은 한 방향에서만 이동해 올 수 있기 때문에 따로 초기화한다.
        그 이후에 (1,1)부터 (n-1, m-1)까지 돌면서 해당 좌표의 10, 12, 9시 중에 사탕 개수가 가장 큰 좌표를 선택하고 거기에 해당 좌표에서 얻을 수 있는 사탕의 개수를 추가한다.
'''
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]* m for _ in range(n)]
dy[0][0] = arr[0][0]
for i in range(1, m):
    dy[0][i] = dy[0][i-1] + arr[0][i]
for i in range(1, n):
    dy[i][0] = dy[i-1][0] + arr[i][0]
for i in range(1, n):
    for j in range(1, m):
        dy[i][j] = max(dy[i-1][j-1], dy[i-1][j], dy[i][j-1]) + arr[i][j]
print(dy[n-1][m-1])
