from collections import deque

def solution(progresses, speeds):
    day = deque() # 남은 일수 큐
    answer = [] 
    for i in range(len(progresses)) :
        if ( (100-progresses[i]) % speeds[i] ==0):
            day.append((100-progresses[i]) // speeds[i])
        else:
            day.append((100-progresses[i]) // speeds[i] + 1)

    cnt = 1 # 배포 개수 무조건 1개이상

# 큐에서 현재 일수를 하나씩 꺼내 비교하면서 배포개수를 세는 방법.. 너무 어려웠다
    while (day) :
        if cnt > 1: 
            cnt -= 1 # 2개이상이면 cnt를 1로 초기화해줘서 일수 다시 계산
            now_progress_day=day.popleft()
            continue
        
        now_progress_day = day.popleft()
        for progress_day in day:
            if now_progress_day >= progress_day:
                cnt += 1
            else:
                break
        answer.append(cnt) # 개수 정답 리스트에 저장
    return answer

print(solution([93, 30, 55] , [1, 30, 5]))
