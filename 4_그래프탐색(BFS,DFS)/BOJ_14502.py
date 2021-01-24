'''
    문제설명
        백준 14502 연구소(BFS 이용)
        벽 3개 세워서 바이러스로부터의 안전영역 최댓값 구하기
    해결전략
        바이러스도 없고 기존에 벽도 없는 빈칸에 벽 3개를 세워야한다. 
        완전탐색을 이용해서 주어진 2차원 리스트에 값이 0인 좌표에 벽을 3개 세울 수 있는 모든 방법을 탐색한다.
        선택된 3개의 좌표에 벽을 세우고 주어진 2차원 리스트를 깊은 복사해서 매번 새롭게 바이러스가 퍼지는 결과를 검증한다.
        바이러스가 있는 좌표에서 상하좌우의 좌표가 범위 안에 속하고 빈칸일 때 바이러스가 퍼지도록 BFS를 이용해 구현한다.
        BFS을 마치고 나면 2차원 리스트에서 행단위로 0의 개수를 세서 기존 안전 영역의 최댓값과 비교해서 더 크면 갱신한다.
'''

import sys
import copy
from collections import deque
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
maxx = -2147000000

def BFS():
    global maxx
    tmp_arr = copy.deepcopy(arr)
    Q = deque()
    for i in range(n):
        for j in range(m):
            if tmp_arr[i][j] == 2:
                Q.append((i, j))
    while Q:
        a, b = Q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and tmp_arr[x][y] == 0:
                Q.append((x, y))
                tmp_arr[x][y] = 2
    res = sum(i.count(0) for i in tmp_arr)
    maxx = max(maxx, res)

def select_wall(cnt):
    if cnt == 3:
        BFS()
    else:
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    select_wall(cnt + 1)
                    arr[i][j] = 0

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

select_wall(0)
print(maxx)