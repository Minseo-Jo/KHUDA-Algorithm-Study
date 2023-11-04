def solution(arr):
    answer = []
    n = len(arr)
    
    for i in range(n-1):
        if (arr[i] != arr[i+1]):
            answer.append(arr[i])
            
    # 마지막 요소는 직접 넣어줘야함
    answer.append(arr[-1])
    
    return answer