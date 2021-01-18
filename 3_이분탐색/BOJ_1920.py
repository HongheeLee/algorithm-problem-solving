'''
    문제설명
        백준 1920 (이분탐색 이용)
        n개의 정수가 주어져 있을 때 이 안에 x라는 정수가 존재하는지 알아내는 프로그램 작성
    해결전략
        n개의 정수를 이분 탐색을 위해 먼저 정렬한다.
        x가 n개의 정수 중 가장 작은 수보다 작거나 가장 큰수보다 크면 존재하지 않는다고 할 수 있다.
        만약 그 범위 사이에 있다면 이분탐색을 진행한다.
        가장 작은 수의 인덱스를 lt, 가장 큰 수의 인덱스를 rt로 놓고 그 가운데 위치한 값을 기준으로 x의 위치를 탐색한다.
        x가 중간값보다 크면 lt를 mid+1로 이동시키고, x가 중간값보다 작으면 rt를 mid-1로 이동시켜서 탐색의 범위를 줄인다.
        탐색하면서 일치하는 값을 발견하면 1을 출력하고 함수를 종료한다.
        탐색을 모두 마쳤을 때(lt가 rt보다 커졌을 때)에도 함수가 종료되지 않았으면 일치하는 값을 찾지 못한 것이므로 0을 출력한다.
'''
def check(x):
    lt = 0
    rt = n-1
    if x < a[lt] or x > a[rt]:
        print(0)
        return
    while lt <= rt:
        mid = (lt + rt) // 2
        if x == a[mid]:
            print(1)
            return
        elif x > a[mid]:
            lt = mid + 1
        elif x < a[mid]:
            rt = mid - 1
    print(0)
n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))
for k in b:
    check(k)