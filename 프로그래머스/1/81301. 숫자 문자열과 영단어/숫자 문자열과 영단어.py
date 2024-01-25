def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for idx, word in enumerate(words):
        if word in s:
            s=s.replace(word,str(idx))
    return int(s)
    # i=0
    # st=''
    # while i < len(s):
    #     if s[i]=='z':
    #         st+='0' 
    #         i+=4
    #     elif s[i]=='o':
    #         st+='1'
    #         i+=3
    #     elif s[i]=='t':
    #         if s[i+1]== 'w':
    #             st+='2'
    #             i+=3
    #         else:
    #             st+='3'
    #             i+=5
    #     elif s[i]=='f':
    #         if s[i+1]== 'o':
    #             st+='4'
    #             i+=4
    #         else:
    #             st+='5'
    #             i+=4 
    #     elif s[i]=='s':
    #         if s[i+1]== 'i':
    #             st+='6'
    #             i+=3
    #         else:
    #             st+='7'
    #             i+=5
    #     elif s[i]=='e' :
    #         st+='8'
    #         i+=5
    #     elif s[i]=='n':
    #         st+='9'
    #         i+=4
    #     else:
    #         st+=str(s[i])
    #         i+=1
    # return int(st)