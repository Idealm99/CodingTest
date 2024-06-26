# 기본 모듈

## zip(반복 가능한 객체,) 
* 반복 가능한 객체: 리스트, 튜플, 문자열 등 반복 가능한 객체 (개수가 동일해야 함)

* 사용 방법 1
```
# 이름과 나이를 묶어 튜플 리스트 만들기
names = ["Alice", "Bob", "Carol"]
ages = [20, 25, 30]

people = zip(names, ages)

print(people)  # [('Alice', 20), ('Bob', 25), ('Carol', 30)]

```
* 사용 방법 2

```
def a(n):
  return n*2

li=[1,2,3,4,5]
k=map(a,li)
print(list(k)) # [2, 4, 6, 8, 10]
```

## map(함수, 반복 가능한 객체)

```
# 리스트의 각 숫자에 2를 곱하여 새로운 리스트 만들기
numbers = [1, 2, 3, 4, 5]

def double(x):
    return x * 2

doubled_numbers = map(double, numbers)

print(doubled_numbers)  # [2, 4, 6, 8, 10]

```

## 사전

* 사전에서 key값으로 리스트는 안되고 튜플은 가능하다

```
my_dict = {
    ("key1", "value1"): "value2",
    ("key2", "value2"): "value3",
}


my_dict[("key1", "value1")] # value2
```

## lstrip / rstrip (가장 왼/오른쪽 삭제하기)

```
a='01110'
b= a.lstrip('0') # 1110
c= a.rstrip('0') # 0111
```

## replace

```
a = '111'
a.replace('1','0') # '000'
```


# collections 모듈

## Counter

```
import collections
cnt = collections.Counter(tangerine)

```
위 코드로 유닛의 개수를 사전 형식으로 한번에 구할 수 있다.

## defaultdict

```
from collections import defaultdict


    # 각 종류의 옷이 몇 개 있는지를 defaultdict를 사용해 카운트합니다.
    counts = defaultdict(int)
    for item, category in clothes:
        counts[category] += 1
```

# itertools 모듈듈

## combinations( 조합을 계산할 대상 컬렉션 , 선택할 원소의 개수)

* 사용방법

```
from itertools import combinations

# 5개의 숫자 중 3개를 선택하는 조합 모두 출력
numbers = [1, 2, 3, 4, 5]

for comb in combinations(numbers, 3):
    print(comb)

# (1, 2, 3)
# (1, 2, 4)
# (1, 2, 5)
# (1, 3, 4)
# (1, 3, 5)
# (1, 4, 5)
# (2, 3, 4)
# (2, 3, 5)
# (2, 4, 5)
# (3, 4, 5)
```

## ChainMap( 사전1, 사전2) - 사전 합치기

* 사용 방법
  
```
from itertools  import ChainMap

user_config = {"name": "Bard"}
default_config = {"language": "python"}

# 기본 설정을 우선시하는 설정 맵 생성
combined_config = ChainMap(user_config, default_config)

print(combined_config["name"])  # Bard
print(combined_config["language"])  # python
```

