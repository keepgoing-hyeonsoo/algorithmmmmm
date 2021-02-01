📅 Date: 2021-01-26 (화)

# 18222. 투에-모스 문자열
출처: https://www.acmicpc.net/problem/18222

## 📝 Problem

### 문제

0과 1로 이루어진 길이가 무한한 문자열 X가 있다. 이 문자열은 다음과 같은 과정으로 만들어진다.

X는 맨 처음에 "0"으로 시작한다. 
X에서 0을 1로, 1을 0으로 뒤바꾼 문자열 X'을 만든다.
X의 뒤에 X'를 붙인 문자열을 X로 다시 정의한다. 
2~3의 과정을 무한히 반복한다.
즉, X는 처음에 "0"으로 시작하여 "01"이 되고, "0110"이 되고, "01101001"이 되고, ⋯ 의 과정을 거쳐 다음과 같이 나타내어진다.

    "011010011001011010010110011010011001011001101001⋯⋯"

자연수 k가 주어졌을 때 X의 k번째에는 무슨 문자가 오는지 구하여라.

### 입력

첫 번째 줄에 자연수 k (1 ≤ k ≤ 1018) 가 주어진다.

### 출력

첫 번째 줄에 k번째에 오는 문자를 출력하라.

## Input/Output example

### Input

```
1
```

### Output

```
0
```

### Input

```
2
```

### Output

```
1
```

### Input

```
10
```

### Output

```
0
```

# ✅ Submit
## 👌 Solved Code 

### 💡 Idea

규칙을 찾아서 점화식만 만들면 해결되는 문제였다. 문자열의 갯수는 1,2,4,8,16.. 으로 2의 거듭제곱 형태로 커지는 것에 착안하면 2의 거듭제곱과 관련된 규칙이 있을 것이라는 추측을 할 수 있다.  
<br>
점화식 문제는 재귀함수를 이용한다. 대표적인 예로 팩토리얼과 피보나치 문제가 있다.

### 💻 Code
(Important part only)

``` python
import sys

k = int(sys.stdin.readline())

def recursion(x):
    if (x==1):
        return 0

    N = maxPowerOf2(x)
    
    return 1-recursion(x-N)

# n보다 작은 수 중 가장 큰 2의 거듭제곱수를 찾는 함수
def maxPowerOf2(n):
    m = 0
    while( 2 ** m < n ):
        m += 1
    
    return 2 ** (m-1)

print(recursion(k))
```

### ✍ Solution
문자열의 문자 갯수를 2^k 개라고 했을때, `1번째부터 2^(k-1)번째` 와  `2^(k-1) + 1 번째 부터 2^k` 를 비교해보면 앞과 뒤가 반전된 형태이다.
x번째 문자를 f(x) 라고 정의하고, x 보다 작은 수 중에서 가장 큰 2의 거듭제곱 수를 N 이라고 하자.  
그러면 `f(x) + f(x-N) = 1` 이라는 점화식이 성립한다.

### 💬 Commentary
- 규칙 찾는 것이 어려웠다. 점화식 찾는 것이 사실상 전부였다.

## References
- https://m.blog.naver.com/jh05013/221750300422