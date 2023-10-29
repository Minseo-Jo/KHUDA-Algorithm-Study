
#이진 검색 함수 정의
def binarysearch(array, target, start, end):
    while start <= end :
        mid = (start + end) // 2

        # 중간부터 찾기 시작, 찾으면 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간값보다 작다면 왼쪽 범위 search
        elif array[mid] > target :
            end = mid -1
        # 중간값보다 크다면 오른쪽 범위 search
        else:
            start = mid + 1
    return None

# 입력
# N 요소 개수 입력
n = int(input())

# 공백으로 구분하여 N개의 요소 입력
N_array = list(map(int, input().split()))

#오름차순 정렬 진행
N_array.sort()

#M 요소 개수 입력
m = int(input())

# 공백으로 구분하여 M개의 요소를 입력
M_array = list(map(int, input().split()))


# 손님이 요청한 M개의 요소를 확인하며 이진 탐색 수행
for i in M_array :
    result = binarysearch(N_array, i, 0, n-1) # 인덱스니까 0~n-1까지
    if result != None :
        print('yes', end = ' ') # 출력 조건 줄바꿈이 아님 띄어쓰기임 ! 주의
    else:
        print('no', end = ' ')





               
