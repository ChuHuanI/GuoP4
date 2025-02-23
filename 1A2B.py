import random

def generate_answer():
    # 生成一個四位不重複的隨機數字作為答案
    numbers = list(range(10))
    random.shuffle(numbers)
    return ''.join(map(str, numbers[:4]))

def calculate_score(guess, answer):
    # 計算 A 和 B 的數量
    A = sum(guess[i] == answer[i] for i in range(4))
    B = sum(min(guess.count(digit), answer.count(digit)) for digit in set(guess)) - A
    return A, B

def main():
    print("歡迎來到 1A2B 猜數字遊戲！")
    answer = generate_answer()
    attempts = 0

    while True:
        guess = input("請輸入四位不重複的數字（輸入 A 公布答案，輸入 X 離開）：")
        if guess.upper() == 'A':
            print(f"答案是：{answer}")
            break
        
        if guess.upper() == 'X':
            print("遊戲已退出。再見！")
            break

        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("輸入錯誤，請重新輸入四位不重複的數字。")
            continue

        attempts += 1
        A, B = calculate_score(guess, answer)
        print(f"結果：{A}A{B}B")

        if A == 4:
            print(f"恭喜你猜對了！總共猜了 {attempts} 次。")
            break

if __name__ == "__main__":
    main()
