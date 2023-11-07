

# 리스트 원소 개수 입력
n = int(input())

# 하나씩 입력된 수를 array에 추가
array = []

for i in range (n):
    array.append(int(input()))

# 파이썬 정렬 라이브러리 sort 를 쓰면 코드가 훨씬 간결해짐
array.sort(reverse=True)

# 원소 하나씩 출력
for i in range (n) :
    print(array[i], end=' ')


