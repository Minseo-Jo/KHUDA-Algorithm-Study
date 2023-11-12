def solution(players, callings):
    # {등수 : 선수} , {선수: 등수} 딕셔너리 생성
    idx = {i : player for i,player in enumerate(players)}
    p = {player : i for i,player in enumerate(players)}
    
    for i in callings :
        current_rank = p[i]
        foward_rank = current_rank-1
        foward_player = idx[foward_rank]
        
        #player swap
        idx[current_rank] = foward_player 
        idx[foward_rank] = i
        
        # rank swap
        p[i] = foward_rank
        p[foward_player] = current_rank
        
        
    return list(idx.values())