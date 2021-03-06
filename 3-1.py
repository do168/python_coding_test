"""
그리디 - 거스름돈 - 그리디 알고리즘은 기준에 따라 좋은 것을 선택하는 알고리즘
                - 문제를 잘 분석해서 '현재 상황에서 지금 당장 좋은 것만 고른다'
                - 알게 모르게 '가장 큰 순서대로', '가장 작은 순서대로' 같은 기준을 제시한다.
                - 그리디로 문제를 풀 경우 이용한 그리디 알고리즘의 정당성을 검토하여야 한다.
"""

# 거스름돈이 1260원일 때 가장 적은 수의 동전을 사용하는 방법은? => 단위가 큰 동전부터 빼준다.
# 이러한 그리디 알고리즘이 정당한지 검토하자. 현재 화폐의 단위는 큰 단위가 작은 단위의 배수이다. 즉 작은 단위만 아무리 많이 해도 결국 큰 단위로
# 표현이 가능한 단위들의 조합이기 때문에 정당하다.
n = 1260
cnt = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    # 현재 동전으로 채울 수 있는 수
    cnt += n // coin
    # 현재 동전으로 채운 뒤 남은 거스름돈
    cnt %= coin

print(cnt)
