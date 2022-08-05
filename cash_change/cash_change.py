def calculate_change(payment, cost):
    # 코드를 작성하세요.
    val = payment - cost
    oman = val // 50000
    man = (val - (oman * 50000)) // 10000
    ochn = (val - (oman * 50000) - (man * 10000)) // 5000
    chn = (val - (oman * 50000) - (man * 10000) - (ochn * 5000)) // 1000
    
    print("""50000원 지폐: {}장
10000원 지폐: {}장
5000원 지폐: {}장
1000원 지폐: {}장""".format(oman, man, ochn, chn))

# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)