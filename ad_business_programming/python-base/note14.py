# 리스트 마지막 원소는 실제 점수가 아닌 음수로 저장되어 있음
# 확장: 평균점수 구하기
def out_min(a):
    i = 0
    min_a = 1000
    while a[i] > 0:
        if a[i] < min_a:
            min_a = a[i]
        i += 1
    return min_a

def out_max(a):
    i = 0
    max_a = 0
    while a[i] > 0:
        if a[i] > max_a:
            max_a = a[i]
        i += 1
    return max_a

def avg(a):
    i = 0
    nsum = 0
    while a[i] > 0:
        nsum += a[i]
        i += 1
    return nsum / i


score = [10, 50, 40, 90, 45, 77, 100, 25, -1]
print(out_min(score))
print(out_max(score))
print(avg(score))