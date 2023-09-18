import re

search_text = input("Enter an email what you will find.")
at_index = search_text.find('@')
if at_index != -1:
    domain = search_text[at_index + 1:]
else:
    print("Worng email form")
    exit()

file_path = input("Enter path")

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()

        pattern = f'\\b\\w+@{re.escape(domain)}\\b'
        matches = re.findall(pattern, file_contents)

        if matches:
            print(f"email domain: {domain}")
            for match in matches:
                print(match)
        else:
            print(f"I couldn't find {domain} in the text file.")
except FileNotFoundError:
    print(f"I couldn't find '{file_path}'")
except Exception as e:
    print(f"Error: {str(e)}")
