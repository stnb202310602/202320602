def rev_str(s):
    # 종료 조건: 문자열이 비어있을 때
    if len(s) == 0:
        return s
    else:
        # 문자열의 첫 번째 문자와 나머지 문자열을 뒤집어 합칩니다.
        return rev_str(s[1:]) + s[0]

if __name__ == '__main__':
    print(rev_str('ABCDE'))
    print(rev_str('Come again, Forever young!'))
    print(rev_str('Amore, Roma'))
