import random


def up_down_game():
    while True:
        print("=== Up Down 게임을 시작합니다 ===")
        number = random.randint(1, 100)
        attempts = 0

        while True:
            try:
                guess = int(input("1에서 100 사이의 숫자를 입력하세요: "))
                attempts += 1

                if guess < 1 or guess > 100:
                    print("잘못된 입력입니다. 1에서 100 사이의 숫자를 입력하세요.")
                    continue

                if guess < number:
                    print("Up! 더 큰 숫자를 입력하세요.")
                elif guess > number:
                    print("Down! 더 작은 숫자를 입력하세요.")
                else:
                    print(f"정답입니다! {attempts}번 만에 맞추셨습니다.")
                    break

            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력하세요.")
                continue

        play_again = input("다시 하시겠습니까? (yes/no): ").lower()
        if play_again != 'yes':
            print("게임을 종료합니다.")
            break


if __name__ == "__main__":
    up_down_game()
