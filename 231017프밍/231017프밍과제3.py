from collections import Counter

def preprocess_text(text):

    cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)
    return cleaned_text.split()

def read_file(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return preprocess_text(text)

def compare_word_frequencies(file1_path, file2_path):
    
    words1 = read_file(file1_path)
    words2 = read_file(file2_path)

    counter1 = Counter(words1)
    counter2 = Counter(words2)

    common_words = set(words1) & set(words2)

    print("공통된 단어와 각 파일에서의 빈도:")
    for word in common_words:
        file1 = counter1[word]
        file2 = counter2[word]
        print(f"{word}: 파일1={file1}, 파일2={file2}")

file1_path = "/Users/kim_seong_kyeong/Library/CloudStorage/OneDrive-우송대학교(WOOSONGUNIVERSITY)/프로그래밍/231017프밍/06 file01.txt"  # 파일1 경로
file2_path = "/Users/kim_seong_kyeong/Library/CloudStorage/OneDrive-우송대학교(WOOSONGUNIVERSITY)/프로그래밍/231017프밍/06 file02.txt"  # 파일2 경로

compare_word_frequencies(file1_path, file2_path)