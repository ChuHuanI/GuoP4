import random

def print_board(board):
    """
    顯示數字拼圖的盤面。
    """
    for row in board:
        print(" | ".join(str(num) if num != 0 else " " for num in row))
        print("-" * (len(board) * 4 - 1))


def is_valid_move(board, row, col, num):
    """
    檢查在特定位置放置數字是否有效。
    """
    # 檢查該列是否有重複數字
    if num in board[row]:
        return False

    # 檢查該行是否有重複數字
    for r in range(len(board)):
        if board[r][col] == num:
            return False

    return True


def get_empty_position(board):
    """
    找到第一個空的位置。
    """
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return row, col
    return None


def initialize_board(size):
    """
    初始化拼圖盤面並預填數字。
    """
    board = [[0 for _ in range(size)] for _ in range(size)]
    for _ in range(size):
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        num = random.randint(1, size)
        if board[row][col] == 0 and is_valid_move(board, row, col, num):
            board[row][col] = num
    return board


def play_game():
    """
    啟動數字拼圖遊戲。
    """
    # 選擇遊戲模式
    while True:
        size_choice = input("請選擇遊戲模式 (A: 3x3, B: 5x5, C: 7x7, D: 9x9) 或按 X 離開: ").strip().upper()
        if size_choice == 'A':
            size = 3
            break
        elif size_choice == 'B':
            size = 5
            break
        elif size_choice == 'C':
            size = 7
            break
        elif size_choice == 'D':
            size = 9
            break
        elif size_choice == 'X':
            print("遊戲已退出。")
            return
        else:
            print("請輸入有效的選項 (A, B, C, D 或 X)！")

    board = initialize_board(size)
    history = []  # 用於記錄歷史狀態

    print(f"歡迎來到 {size}x{size} 數字拼圖遊戲！")
    print(f"請將 1 到 {size} 填入盤面，每列與每行的數字不能重複！\n")

    while True:
        print_board(board)
        position = get_empty_position(board)

        if not position:
            print("恭喜你完成拼圖！")
            break

        row, col = position
        user_input = input(f"請輸入 1 到 {size} 的數字 (位置: row {row + 1}, col {col + 1})，按 B 返回上一步，按 A 顯示解答，按 X 離開: ").strip().upper()

        if user_input == 'X':
            print("遊戲已退出。")
            break

        if user_input == 'B':
            if history:
                board = history.pop()
                print("已返回上一步！")
            else:
                print("無法返回，這是第一步！")
            continue

        if user_input == 'A':
            print("顯示完整解答：")
            print_board(board)
            continue

        try:
            num = int(user_input)
            if num < 1 or num > size:
                print(f"請輸入有效數字 1 到 {size}！")
                continue

            if is_valid_move(board, row, col, num):
                # 儲存當前狀態到歷史紀錄
                history.append([row[:] for row in board])
                board[row][col] = num
            else:
                print("數字無法放置在該位置，請重新輸入！")
        except ValueError:
            print("請輸入有效的整數、B 返回上一步、A 顯示解答或 X 離開！")

if __name__ == "__main__":
    play_game()
