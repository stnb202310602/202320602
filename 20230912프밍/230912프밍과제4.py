import re

file_path = "/Users/kim_seong_kyeong/Library/CloudStorage/OneDrive-우송대학교(WOOSONGUNIVERSITY)/프로그래밍/mbox.txt"

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()

        matches = re.findall(r'New Revision: (\d+)', file_contents)

        if matches:
            numbers = [int(match) for match in matches]

            count = len(numbers)
            total = sum(numbers)

            if count > 0:
                average = total / count
                print(f"total {count} lines are matched")
                print(f"average: {average}")
            else:
                print("I couldn't find anything")
        else:
            print("I couldn't find anything")
except FileNotFoundError:
    print(f"I can't find '{file_path}'.")
except Exception as e:
    print(f"Error: {str(e)}")
