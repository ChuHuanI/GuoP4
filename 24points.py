import random
import itertools

def generate_numbers():
    """隨機生成有解的四個數字組合"""
    while True:
        numbers = [random.randint(1, 10) for _ in range(4)]
        solutions = find_24_solutions(numbers)
        if solutions:
            return numbers, solutions

def find_24_solutions(numbers):
    """尋找所有可能的 24 點解法（保持數字順序）"""
    operators = ['+', '-', '*', '/']
    solutions = set()  # 用 set 避免重複解

    for ops in itertools.product(operators, repeat=3):
        expressions = [
            f"({numbers[0]}{ops[0]}{numbers[1]}){ops[1]}({numbers[2]}{ops[2]}{numbers[3]})",
            f"(({numbers[0]}{ops[0]}{numbers[1]}){ops[1]}{numbers[2]}){ops[2]}{numbers[3]}",
            f"{numbers[0]}{ops[0]}(({numbers[1]}{ops[1]}{numbers[2]}){ops[2]}{numbers[3]})",
            f"{numbers[0]}{ops[0]}({numbers[1]}{ops[1]}({numbers[2]}{ops[2]}{numbers[3]}))"
        ]
        for expr in expressions:
            try:
                if abs(eval(expr) - 24) < 1e-6:
                    solutions.add(expr)  # 加入解答集合
            except ZeroDivisionError:
                continue

    return list(solutions) if solutions else None

def play_24_game():
    print("歡迎來到 24 點數字遊戲！")
    print("請輸入有效的算式來計算出 24，或輸入 'A' 顯示所有正確解答，'X' 結束遊戲。")

    while True:
        numbers, solutions = generate_numbers()
        print("\n本題的數字是：", numbers)

        while True:
            expression = input("請輸入你的算式（或輸入 'A' 顯示答案，'X' 結束遊戲）： ").strip().upper()
            
            if expression == 'X':
                print("感謝遊玩，再見！👋")
                return
            
            if expression == 'A':
                print("所有可能的解法（固定數字順序）：")
                for sol in solutions:
                    print(f"✅ {sol}")
                break  # 顯示答案後換下一題

            # 驗證玩家輸入
            try:
                result = eval(expression)
                if abs(result - 24) < 1e-6:
                    print("恭喜！你成功計算出 24！🎉")
                    break  # 進入下一題
                else:
                    print(f"結果是 {result}，再試一次！")
            except (SyntaxError, ZeroDivisionError, NameError):
                print("算式不合法，請重新輸入有效的算式！")

play_24_game()
