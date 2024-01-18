def solution(bandage, health, attacks):
    healing_time, healing, addition_heal = bandage 
    
    hp=health
    heal_count =0
    last=attacks[-1][0]+1
    # i 는 전체 시간 흐름
    for i in range (1, last):
      for at, ad in attacks : 
        if i == at :
          hp -= ad
          heal_count =0
          if hp <= 0 :
            return -1
          attacks.pop(0)
          break
        
        
        hp += healing
        heal_count +=1
        if hp > health :
            hp = health
        
        if heal_count == healing_time:
          hp = hp + addition_heal
          if hp > health:
            hp = health
          heal_count=0
        break
    return hp