'''
    문제설명
        백준 10815 숫자카드 (이분탐색 이용)
        숫자 카드 N개가 있을 때 주어진 정수가 적힌 숫자카드를 가지고 있는지 아닌지를 구하는 프로그램.
    해결전략
        가지고 있는 숫자카드를 정렬해서 주어진 정수마다 이분탐색을 수행한다.
        가장 작은 수의 인덱스를 lt, 가장 큰 수의 인덱스를 rt로 놓고 그 중간값과 주어진 정수를 비교한다.
        주어진 정수가 중간값이 같으면 1을 출력하고 함수를 종료한다.
        주어진 정수가 더 크면 lt를 mid + 1로 바꾸고 중간값이 더 크면 rt를 mid -1로 바꿔 탐색의 범위를 좁힌다.
        탐색이 완료되었는데도 함수가 종료되지 않았으면 숫자카드 내에 주어진 정수가 존재하지 않는 것이므로 0을 출력한다.
'''
import sys
def check(x):
    lt = 0
    rt = n-1
    while lt <= rt:
        mid = (lt+rt) // 2
        if x == a[mid]:
            print(1, end=' ')
            return
        elif x < a[mid]:
            rt = mid - 1
        elif x > a[mid]:
            lt = mid + 1
    print(0, end = ' ')
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(input())
b = list(map(int, sys.stdin.readline().split()))
a.sort()
for x in b:
    check(x)