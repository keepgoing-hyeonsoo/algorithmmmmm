import heapq
import sys

# in1 ~ in5.txt 파일입력을 쉽게 하기 위한 for문
for fileNum in range(1, 6):
    # for fileNum in range(6, 7):
    print(f"---입력예시 {fileNum}---")
    fileName = f"in{fileNum}.txt"
    sys.stdin = open(fileName, "rt")

    # 로직 시작
    max_heap = []

    while True:
        n = int(sys.stdin.readline().rstrip())
        if n == 0:
            if not max_heap:
                print("-1")
                break
            print(heapq.heappop(max_heap)[1])
        elif n == -1:
            break
        else:
            heapq.heappush(max_heap, (-n, n))

    # 로직 끝
