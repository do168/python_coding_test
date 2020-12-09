"""
그리디 - 큰수의 법칙 - 정렬 후 최대 인덱스를 K만큼 곱한 뒤 그 다음 수를 1번 더해준다. 이 과정을 M까지 반복
"""

import sys

N, M, K = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

array.sort(reverse=True)

first = array[0]
second = array[1]
answer = 0
# M이 100억 미만일 때 가능한 방법.
# while True:
#     for i in range(K):
#         if M == 0:
#             break
#         answer += first
#         M -= 1
#
#     if M == 0:
#         break
#     answer += second
#     M -= 1

# N이 100억 이상일 때 -> 수학적인 방법을 이용해야 한다. 최대값을 K번, 차대값을 1번 더하므로 M번 안에서 이 과정은 M / (K+1) 번 반복한다
# 최대값은 즉 M / (K+1) 과정 안에서 K번 반복하고, 남은 횟수만큼 또 반복한다.
cnt = int(M / (K+1)) * K
cnt += M % (K+1)

answer += first * cnt
# 차대값은 제한된 M번의 횟수 중 최대값의 반복횟수를 뺀 값만큼 반복한다.
answer += (M - cnt) * second

print(answer)


