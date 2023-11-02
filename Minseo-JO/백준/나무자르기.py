# n : 나무의 수, m : 가져가려는 나무 길이
n, m = map(int, input().split())
trees = list(map(int,input().split()))

start, end = 1, max(trees)

while (start <= end):
    mid = (start+end)//2 
    cnt = 0
    for tree in trees:
        if tree >= mid :
            cnt += tree-mid
            
    if cnt < m : # 가져갈 수 있는 나무 길이가 m 보다 작다면
        end = mid -1 # 높이가 낮은 나무 내에서 다시 계산
    else: # 가져갈 수 있는 나무의 길이가 m과 
        start = mid + 1 
        
print(end)