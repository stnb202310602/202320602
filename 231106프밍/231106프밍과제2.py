number = input("스페이스바로 정수 10개를 입력하시오").split()

if len(number) == 10:

    numbers = [int(i) % 42 for i in number if 0 < int(i) <= 1000]

    print(len(set(numbers)))
    