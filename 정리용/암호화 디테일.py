import tkinter as tk
from tkinter import filedialog

# 암호화 함수: XOR 연산을 사용하여 입력된 텍스트를 암호화.
def Lock(text, key):
    lockText = []  # 암호화된 문자를 저장할 리스트
    k_leng = len(key)  # 키의 길이
    encryptedKey = [ord(char) for char in key]  # 키 문자열을 숫자(ASCII)로 변환하여 리스트에 저장

    for i, char in enumerate(text):
        char_ord = ord(char)  # 현재 문자에 대한 ASCII 코드
        key_digit = encryptedKey[i % k_leng]  # 키의 해당 위치에 있는 숫자 (순환 참조)
        encrypted_char = char_ord ^ key_digit  # XOR 연산을 통해 문자 암호화
        lockText.append(encrypted_char)  # 암호화된 문자를 리스트에 추가

    return lockText  # 암호화된 문자들의 리스트 반환

# 복호화 함수: 암호화된 텍스트를 XOR 연산으로 원래의 텍스트로 복원합니다.
def decrypt(encrypted_text, key):
    decrypted_text = []  # 복호화된 문자들을 저장할 리스트
    key_len = len(key)  # 키의 길이
    key_ord = [ord(char) for char in key]  # 키 문자열을 숫자(ASCII)로 변환하여 리스트에 저장

    for i, encrypted_char in enumerate(encrypted_text):
        key_digit = key_ord[i % key_len]  # 키의 해당 위치에 있는 숫자 (순환 참조)
        original_char = chr(encrypted_char ^ key_digit)  # XOR 연산을 통해 원래 문자 복원
        decrypted_text.append(original_char)  # 복원된 문자를 리스트에 추가

    return ''.join(decrypted_text)  # 복호화된 문자들을 문자열로 반환

# 암호화된 데이터를 파일에 저장하는 함수
def save_encrypted_data(encrypted_data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        # 각 암호화된 데이터를 4자리 16진수로 변환하여 파일에 저장
        hex_data = ''.join([hex(data)[2:].zfill(4) for data in encrypted_data])
        f.write(hex_data)  # 변환된 16진수를 파일에 기록

# 암호화된 데이터가 저장된 파일을 로드하는 함수
def load_encrypted_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        hex_data = f.read().strip()  # 파일에서 16진수 데이터 읽기
        # 16진수를 4자리씩 나누어 각각을 정수로 변환
        encrypted_data = [int(hex_data[i:i+4], 16) for i in range(0, len(hex_data), 4)]
    return encrypted_data  # 암호화된 데이터를 반환

# 파일을 선택하는 함수 (파일 탐색기 열기)
def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])  # 텍스트 파일만 선택 가능
    if filename:  # 파일이 선택되었다면
        file_entry.delete(0, tk.END)  # 기존 입력된 파일 경로 지우기
        file_entry.insert(0, filename)  # 선택된 파일 경로 입력란에 넣기

# 입력된 내용을 파일에 저장하는 함수
def save_file(content, title):
    file_path = file_entry.get()  # 현재 파일 경로 가져오기
    if not file_path:  # 파일 경로가 비어 있으면
        return  # 아무 동작도 하지 않음
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)  # 내용을 해당 파일에 덮어쓰기

# 암호화 버튼 클릭 시 동작하는 함수
def encrypt_file():
    file_path = file_entry.get()  # 입력된 파일 경로 가져오기
    if not file_path:  # 파일을 선택하지 않으면
        result_text.delete(1.0, tk.END)  # 결과창을 지운 후 오류 메시지 표시
        result_text.insert(tk.END, "파일을 선택하세요.\n")
        return  # 함수 종료
    
    key = key_entry.get()  # 입력된 키값 가져오기
    if not key:  # 키가 비어 있으면
        result_text.delete(1.0, tk.END)  # 결과창을 지운 후 오류 메시지 표시
        result_text.insert(tk.END, "키를 입력하세요.\n")
        return  # 함수 종료

    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # 파일을 읽기 모드로 열기
            text = file.read()  # 파일 내용을 읽어오기

        encrypted_data = Lock(text, key)  # 파일 내용을 암호화

        # 결과창 초기화 및 암호화된 데이터 출력
        result_text.delete(1.0, tk.END)  # 기존 결과 지우기
        result_text.insert(tk.END, "암호화된 데이터:\n")
        
        # 암호화된 데이터를 4자리 16진수로 변환하여 결과창에 출력
        encrypted_hex = ''.join([hex(data)[2:].zfill(4) for data in encrypted_data])
        result_text.insert(tk.END, encrypted_hex + "\n")

        # 암호화된 데이터를 파일에 저장
        save_encrypted_data(encrypted_data, file_path)

    except Exception as e:  # 예외 발생 시 오류 메시지 출력
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"오류 발생: {e}\n")

# 복호화 버튼 클릭 시 동작하는 함수
def decrypt_file():
    file_path = file_entry.get()  # 입력된 파일 경로 가져오기
    if not file_path:  # 파일을 선택하지 않으면
        result_text.delete(1.0, tk.END)  # 결과창을 지운 후 오류 메시지 표시
        result_text.insert(tk.END, "파일을 선택하세요.\n")
        return  # 함수 종료
    
    key = key_entry.get()  # 입력된 키값 가져오기
    if not key:  # 키가 비어 있으면
        result_text.delete(1.0, tk.END)  # 결과창을 지운 후 오류 메시지 표시
        result_text.insert(tk.END, "키를 입력하세요.\n")
        return  # 함수 종료

    try:
        encrypted_data_from_file = load_encrypted_data(file_path)  # 파일에서 암호화된 데이터 로드

        decrypted_text = decrypt(encrypted_data_from_file, key)  # 복호화 진행

        result_text.delete(1.0, tk.END)  # 기존 결과 지우기
        result_text.insert(tk.END, "복호화된 텍스트:\n")
        result_text.insert(tk.END, decrypted_text + "\n")  # 복호화된 텍스트 결과 출력

        save_file(decrypted_text, "복호화된 파일 저장")  # 복호화된 내용을 파일에 저장

    except Exception as e:  # 예외 발생 시 오류 메시지 출력
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"오류 발생: {e}\n")

# 키 입력란의 표시 방식을 토글하는 함수 (숨김/보임)
def toggle_key_visibility():
    current_show = key_entry.cget("show")  # 현재 키 입력란의 "show" 속성 값 가져오기
    if current_show == "":  # 현재 키가 보이는 상태라면
        key_entry.config(show="*")  # 키를 숨김
        key_view_button.config(text="암호보기")  # 버튼 텍스트 변경
    else:
        key_entry.config(show="")  # 키를 보이게 함
        key_view_button.config(text="암호숨기기")  # 버튼 텍스트 변경

# GUI 설정
root = tk.Tk()
root.title("문서 암호화 프로그램")

# 창 크기 조정에 따라 자동으로 크기 변경
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)
root.grid_columnconfigure(2, weight=1)

# 파일 선택 UI
file_label = tk.Label(root, text="암호화할 파일 선택:")
file_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
file_entry = tk.Entry(root, width=40)
file_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
browse_button = tk.Button(root, text="찾아보기", command=browse_file)
browse_button.grid(row=0, column=2, padx=10, pady=10)

# 키 입력 UI (비밀번호처럼 *로 보이게 설정)
key_label = tk.Label(root, text="암호화 키:")
key_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
key_entry = tk.Entry(root, width=40, show="*")  # 키 입력란을 *로 보이게 설정
key_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# 암호보기 버튼 추가 (입력된 키를 보여주는 기능)
key_view_button = tk.Button(root, text="암호보기", command=toggle_key_visibility)
key_view_button.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

# 암호화 버튼과 복호화 버튼
encrypt_button = tk.Button(root, text="암호화", command=encrypt_file)
encrypt_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

decrypt_button = tk.Button(root, text="복호화", command=decrypt_file)
decrypt_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

# 결과 출력 UI
result_label = tk.Label(root, text="결과:")
result_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
result_text = tk.Text(root, width=50, height=10)
result_text.grid(row=3, column=1, padx=10, pady=10, columnspan=2, sticky="nsew")

root.mainloop()
