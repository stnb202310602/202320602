menu_input = input("햄버거 메뉴 3개와 음료 메뉴 2개를 순서대로 스페이스바로 구분해서 입력하시오").split()
if len(menu_input) == 5:
    
    menu_list = []
    try:
        menu_list = [[int(menu_input[i]) for i in range(3)], [int(menu_input[i]) for i in range(3, 5)]]
    except:
        print("숫자만 입력하시오")

    cheap = [min(menu_list[0]), min(menu_list[1])]
    set_disc = cheap[0] + cheap[1] - 50
    print(set_disc)
else:
    print("가격 5개를 스페이스바로 구분해서 입력")