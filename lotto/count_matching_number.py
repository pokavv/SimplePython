def count_matching_numbers(list_1, list_2):
    n = 0
    for i in range(0, len(list_1)):
        for j in range(0, len(list_2)):
            if list_1[i] == list_2[j]:
                n += 1
    return n
    
# 테스트
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))