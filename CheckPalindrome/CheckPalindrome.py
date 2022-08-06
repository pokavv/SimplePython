def check_palindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

input_string = str(input("문자열 입력: "))
check = check_palindrome(input_string)

if check:
    print("회문이 맞음")
else:
    print("회문이 아님")