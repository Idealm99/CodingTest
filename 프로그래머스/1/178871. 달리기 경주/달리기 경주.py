def solution(players, callings):
    player_indices = {player: index for index, player in enumerate(players)}
    for i in callings :
        a=  player_indices[i]
        player_indices[i] -=1
        player_indices[players[a-1]] +=1 
        
        players[a-1], players[a] = players[a], players[a-1]
    return players