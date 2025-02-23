import random

def ultimate_guess_game():
    print("歡迎來到終極密碼遊戲！範圍是 0 到 100。")
    
    # 初始範圍
    lower_bound = 0
    upper_bound = 100

    # 隨機產生答案
    answer = random.randint(lower_bound + 1, upper_bound - 1)
    
    while True:
        try:
            guess = int(input(f"請在 {lower_bound} 到 {upper_bound} 之間猜一個數字："))
            
            # 檢查輸入是否在範圍內
            if guess <= lower_bound or guess >= upper_bound:
                print(f"請輸入有效範圍內的數字 ({lower_bound} ~ {upper_bound})！")
                continue

            # 判斷結果
            if guess < answer:
                print("再大一點！")
                lower_bound = guess
            elif guess > answer:
                print("要小一點！")
                upper_bound = guess
            else:
                print(f"恭喜你！答案就是 {answer}！")
                break
        except ValueError:
            print("請輸入一個有效的整數！")

def main():
    while True:
        ultimate_guess_game()
        play_again = input("是否再開一局？(Y/N)：").strip().upper()
        if play_again != 'Y':
            print("感謝遊玩！再見！")
            break

if __name__ == "__main__":
    main()
