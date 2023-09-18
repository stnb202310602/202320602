import re
input_text = input("이메일을 스페이스바로 구분하여 입력하세요: ")
email_addresses = [email.strip() for email in input_text.split()]
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')
found = False
print("찾은 이메일:")
for email_address in email_addresses:
    matches = email_pattern.findall(email_address)
    if matches:
        found = True
        for match in matches:
            print(match)
if not found:
    print("이메일이 발견되지 않았습니다.")