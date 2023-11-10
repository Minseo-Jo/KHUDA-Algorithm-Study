
#n  : queen개수, nxn 체스판
n = int(input())

ans = 0
row = [0] * n #체스판 초기화
answer_10 = [] # 10번쨰 해를 출력하기 위한 리스트
total_nodes = 0 # 총 노드의 수를 세기 위한 변수


def n_queens(x) :
    global ans, total_nodes, answer_10 # 해의 총 개수를 세기 위해 전역변수 

    if x == n : # 마지막 행(= 마지막 queen)까지 위치시켰다면 해답을 찾은 것
        ans += 1 
        if ans == 10: # 10번째 해를 출력하기 위해 count가 10에 도달했을 때 row copy
            answer_10 = row.copy()
        return
    
    else : # 아직 queen을 다 위치시키지 못한 것이기 x번째 queen을 n개의 열에 한번씩 위치시키면서 유망성 검사
        for i in range (n) :
            total_nodes += 1 # 하나의 열에 둘 때마다 node는 1씩 늘어남 
            row[x] = i # x번째 queen을 i번째 열에 위치시키는 것 = (x, i)에 위치 시키는 것
            if promising(x) :  # 유망하다면 다음 queen에 대해서 유망성 검사
                n_queens(x+1)

def promising(x) : 
    for i in range(x) : # 0부터 x-1행(queen)까지 현재 queen(x)과 2가지 조건을 만족하는지 검사
        if (row[x] == row[i]) or (abs(row[x] - row[i]) == abs(x-i)): # 같은열, 같은 대각선에 위치한다면 false
            return False
    return True


n_queens(0) #0번째 queen부터 시작
print('전체 해의 개수 :', ans)
print('10번째 해 :', answer_10)
print('상태 공간 트리의 모든 노드의 수 :', total_nodes)
