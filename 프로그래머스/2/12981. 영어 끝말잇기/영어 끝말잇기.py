def solution(n, words):
    used_words = set()  # 이미 사용된 단어를 저장할 집합
    last_char = words[0][0]  # 이전 단어의 마지막 문자

    for idx, word in enumerate(words):
        if word in used_words or last_char != word[0]:
            # 이미 사용된 단어인 경우 또는 끝말잇기 규칙에 어긋나는 경우
            return [(idx % n) + 1, (idx // n) + 1]
        else:
            used_words.add(word)  # 단어를 사용된 단어 집합에 추가
            last_char = word[-1]  # 마지막 문자 갱신

    # 모든 단어를 순회했지만 끝말잇기가 끝나지 않은 경우
    return [0, 0]
