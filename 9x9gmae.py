import random
import time

# 遊戲說明
def game_instructions():
    print("歡迎來到九九乘法隨機測驗！")
    print("遊戲規則如下：")
    print("- 一次會出 10 題隨機乘法問題")
    print("- 倒數計時 30 秒")
    print("- 若未在 30 秒內全部答對就算輸了\n")

# 啟動遊戲主程式
def multiplication_quiz():
    game_instructions()
    
    num_questions = 10  # 題目數量
    correct_answers = 0
    time_limit = 30  # 時間限制秒數
    start_time = time.time()  # 計時開始
    total_time_used = 0  # 紀錄作答總時間

    for i in range(num_questions):
        # 檢查是否超過時間限制
        if time.time() - start_time > time_limit:
            print("時間到！你輸了！\n")
            break

        # 隨機生成兩個數字
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)

        # 顯示題目並接收答案
        question_start_time = time.time()
        try:
            user_answer = int(input(f"問題 {i + 1}: {num1} x {num2} = "))
        except ValueError:
            print("請輸入有效的整數！")
            continue

        # 計算作答時間
        question_elapsed_time = round(time.time() - question_start_time, 2)
        total_time_used += question_elapsed_time

        # 檢查答案是否正確
        correct_answer = num1 * num2
        if user_answer == correct_answer:
            print(f"答對了！你花了 {question_elapsed_time} 秒作答，總共使用 {round(total_time_used, 2)} 秒\n")
            correct_answers += 1
        else:
            print(f"答錯了！正確答案是 {correct_answer}。你花了 {question_elapsed_time} 秒作答，總共使用 {round(total_time_used, 2)} 秒\n")

    # 結束遊戲，計算時間
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)

    # 顯示成績
    print("遊戲結束！\n")
    print(f"答對題數: {correct_answers}/{num_questions}")
    print(f"完成時間: {elapsed_time} 秒")

    # 提供重新挑戰的選項
    replay = input("想再挑戰一次嗎？(y/n): ")
    if replay.lower() == 'y':
        multiplication_quiz()
    else:
        print("感謝遊玩，再見！")

# 啟動遊戲
if __name__ == "__main__":
    multiplication_quiz()
