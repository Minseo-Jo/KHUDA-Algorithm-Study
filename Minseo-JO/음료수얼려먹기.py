n, m = map(int,input().split())

graph = []

for i in range (n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    # nxm graph의 범위를 넘어가면 false
    # 인덱스는 0부터 시작하니까 x,y가 n,m인 경우에도 false
    if x <= -1 or x >=n or y <= -1 or y >=m :
        return False
    

    # DFS로 방문한 노드와 연결된 모든 노드까지 한번에 방문하여 표시해주기
    if graph[x][y] == 0 :
        # 방문 표시
        graph[x][y] = 1 
        #현재 위치에서 상,하,좌,우 dfs 재귀 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True #자기 자신은 true return
    return False # graph[x][y] == 1인 경우 이미 방문한 것이니까 False


result = 0
for i in range (n):
    for j in range (m):
        if dfs(i,j): 
            result +=1

print(result)


    


