'''
    문제설명
        백준 2056 작업 (위상 정렬(그래프 정렬) 이용)
        수행해야 할 작업들 사이에 선행관계가 있어서 그 선행관계에 따라 작업할 때 모든 작업을 완료하기 위한 최소시간 구하기
    해결전략
        입력을 바탕으로 각 작업의 선행 작업을 모아놓은 리스트, 후행 작업을 모아놓은 리스트, 걸리는 시간, 선행작업의 수(그래프의 진입차수)를 구성한다.
        선행 작업이 없는 작업을 처음에 모두 큐에 넣고 시작한다.
        큐에서 하나씩 꺼내며 그 작업의 후행 작업들의 선행 작업 수를 1씩 감소시킨다. 그 이후 후행 작업의 선행 작업 수가 0이 되면 그 작업을 큐에 넣는다.
        그리고 시간을 측정하기 위해 큐에 넣은 작업의 선행 작업들 중에서 가장 오래 걸리는 작업의 시간에 해당 작업에 걸리는 시간을 더한다. 
        이 과정을 모두 마치면 time 리스트에는 각 작업을 마칠 때까지 걸린 시간이 표시되게 된다.
        따라서 time 리스트의 최댓값을 출력하면 모든 작업을 완료하기 위한 최소시간이다.
'''
import sys
from collections import deque
n = int(sys.stdin.readline())
dis = [[] for _ in range(n+1)]
rule =[[] for _ in range(n+1)]
degree = [0] * (n+1)
time = [0] * (n+1)
Q = deque()
for i in range(1, n+1):
    res = list(map(int, sys.stdin.readline().split()))
    time[i] = res[0]
    if res[1] == 0:
        continue
    else:
        degree[i] = res[1]
        for j in range(degree[i]):
            dis[i].append(res[j+2])
            rule[res[j+2]].append(i)

for i in range(1, n+1):
    if degree[i] == 0:
        Q.append(i)
while Q:
    tmp = Q.popleft()
    for i in rule[tmp]:
        degree[i] -= 1
        if degree[i] == 0:
            Q.append(i)
            max_time = 0
            for j in dis[i]:
                if max_time < time[j]:
                    max_time = time[j]
            time[i] += max_time
print(max(time))