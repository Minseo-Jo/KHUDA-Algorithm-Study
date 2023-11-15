def solution(n):
    answer = 1
    n = float(n)
    while True:
        if n % answer == 1:
            break
        else:
            answer += 1
    return answer