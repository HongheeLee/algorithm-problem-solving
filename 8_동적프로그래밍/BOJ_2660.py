'''
    문제설명
        백준 2660 회장뽑기 (플로이드 와샬 알고리즘 이용)
        가장 먼 다른 회원과의 거리를 점수로 했을 때 점수가 가장 낮은 사람의 점수와 명수와 번호 구하기.
    해결전략
        모든 정점 쌍에 대해서 최단 거리를 구하는 플로이드 와샬 알고리즘을 이용한다.
        회원의 수가 50명을 넘지 않으므로 최대거리는 50이 넘지 않는다. 따라서 처음 2차원 리스트를 50으로 모두 초기화한다.
        이 때 dis[i][j]는 i 노드에서 j노드로 이동할 때 드는 최소비용이다. 
        이후에 자기 자신으로의 거리는 0이므로 dis[i][i]=0으로 초기화하고 조건에 따라 회원의 정보를 입력받아 인접행렬로 표현해 추가로 초기화한다.
        그리고 플로이드 알고리즘 사용하기 위해 거쳐가는 노드, 시작 노드, 도착 노드 순으로 3중 for문을 이용한다. 
        i 노드에서 j노드로 갈 때 기존 방식과 k 노드를 거쳐가는 방식을 비교해서 더 적은 비용인 방식을 선택하고 이를 dis 리스트에 반영한다. 
        회장이 되는 점수, 명수, 번호를 출력하기 위해 dis의 행별로 최댓값을 구하고 이를 비교해서 최솟값을 갖는 행을 구한다.
'''
n = int(input())
dis = [[50] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dis[i][i] = 0
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dis[a][b] = dis[b][a] = 1
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])

res = [0] * (n+1)
score = 100
for i in range(1, n+1):
    for j in range(1, n+1):
        res[i] = max(res[i], dis[i][j])
    score = min(score, res[i])
print(score, res.count(score))
for i in range(1, n+1):
    if res[i] == score:
        print(i, end= ' ')