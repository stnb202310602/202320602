while True:
    input_str = input("정수를 스페이스바로 구분해서 입력하시오")
    input_list = input_str.split()

    try:
        str_int = [int(x) for x in input_list]
        break
    except ValueError:
        print("정수를 스페이스바로 구분해서 입력하시오")
        continue

def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

result = sum_list(str_int)
print(f"결과: {result}")
