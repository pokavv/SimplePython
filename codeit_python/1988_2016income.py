R = 0.12 #이자율
AP_2016 = 1100000000 #2016 은마아파트 매매가
year = 1988
money = 50000000

while year < 2016:
  money = money * (1 + R)
  year += 1

if money > AP_2016:
  print(f"{int(money - AP_2016)}원 차이로 동일 아저씨 말씀이 맞습니다.")
else:
  print(f"{int(AP_2016 - money)}원 차이로 미란 아주머니 말씀이 맞습니다.")