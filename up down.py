import random

options = ['가위', '바위', '보']


def get_player_choice():
    while True:
        player_choice = input('가위, 바위, 보 중 하나를 선택하세요: ')
        if player_choice in ['가위', '바위', '보']:
            return player_choice
        else:
            print('잘못된 입력입니다. 다시 입력하세요.')


win = 0
draw = 0
lose = 0


while True:
    player_choice = get_player_choice()

    computer_choice = random.choice(options)
    print(computer_choice)

    if (
        (player_choice == '가위' and computer_choice == '보')
            or (player_choice == '바위' and computer_choice == '가위')
            or (player_choice == '보' and computer_choice == '바위')):
        print('이겼음')
        win += 1
    elif player_choice == computer_choice:
        print('비겼음')
        draw += 1
    else:
        print('졌음')
        lose += 1

    retry = input('다시하시겠습니까? (Y/N)').lower()
    if retry == 'y':
        continue
    elif retry == 'n':
        break

print(f"승리 : {win}회 / 비김 : {draw}회 / 패배 : {lose}회")
