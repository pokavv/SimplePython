# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    return krw / 1000
# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    return usd * 125

prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))

i = 0
# prices를 원화(￦)에서 달러($)로 변환하기
for i in range(len(prices)):
    prices[i] = round(krw_to_usd(prices[i]), 1)
    i = i + 1
print("미국 화폐: " + str(prices))

# prices를 달러($)에서 엔화(￥)으로 변환하기
for i in range(len(prices)):
    prices[i] = round(usd_to_jpy(prices[i]), 1)
    i = i + 1
print("일본 화폐: " + str(prices))