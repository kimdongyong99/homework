import random


def get_user_choice():
    while True:
        user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")
        if user_choice in ['가위', '바위', '보']:
            if user_choice == '가위':
                return 1
            elif user_choice == '바위':
                return 2
            elif user_choice == '보':
                return 3
        else:
            print("잘못된 입력입니다. '가위', '바위', '보' 중 하나를 선택하세요.")


def get_computer_choice():
    computer_choice = random.randint(1, 3)
    return computer_choice


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "무승부"
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        return "플레이어 승!"
    else:
        return "컴퓨터 승!"


def main():
    print("=== 가위바위보 게임을 시작합니다 ===")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        if user_choice == 1:
            print("플레이어의 선택: 가위")
        elif user_choice == 2:
            print("플레이어의 선택: 바위")
        elif user_choice == 3:
            print("플레이어의 선택: 보")

        if computer_choice == 1:
            print("컴퓨터의 선택: 가위")
        elif computer_choice == 2:
            print("컴퓨터의 선택: 바위")
        elif computer_choice == 3:
            print("컴퓨터의 선택: 보")

        result = determine_winner(user_choice, computer_choice)
        print(f"결과: {result}")

        play_again = input("다시 하시겠습니까? (y/n): ")
        if play_again.lower() != 'y':
            print("게임을 종료합니다. 감사합니다!")
            break


if __name__ == "__main__":
    main()
