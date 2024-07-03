import random

best = 1e9

while True:
    answer = random.randint(1, 100)
    print(answer)
    count = 0

    if best != 1e9:
        print('이전 최고기록 :', best, '번 입니다.')

    while True:
        user_pick = int(input('1부터 100 사이의 숫자를 입력하세요: '))
        if user_pick < 1 or user_pick > 100:
            print('1부터 100 사이의 숫자를 입력하세요.')
            continue

        count = count + 1
        if user_pick < answer:
            print('UP')
        elif user_pick > answer:
            print('DOWN')
        else:
            print('정답입니다.')
            print(count, '번 만에 맞추셨습니다.')
            best = min(best, count)
            break

    while True:
        retry = input('다시하시겠습니까? (Y/N)')
        retry = retry.lower()
        if retry in ['y', 'yes', 'ok'] or retry in ['n', 'no']:
            break
        else:
            print('Y 또는 N을 입력하세요.')
    if retry in ['y', 'yes', 'ok']:
        continue
    elif retry in ['n', 'no']:
        break
    
print('게임을 종료합니다. 최고기록: ', best)




