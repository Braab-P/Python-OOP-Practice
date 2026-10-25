import random

def play_guess_number():
    x = random.randint(1, 3)
    number_guesses = 0
        
    print("Я загадал число от 1 до 3. У тебя 3 попытки!")
    
    for i in range(3):
        try:
            y = int(input(f"Попытка {i+1}. Твой вариант: "))
            if x == y:
                print('Вау, вы настоящий волшебник!')
                number_guesses += 1
            else:
                print('Увы, в этот раз не повезло!')
        except ValueError:
            print("Пожалуйста, введите целое число.")
            
    print(f'Количество отгадок: {number_guesses}')

    if number_guesses >= 2:
        print('Вау, вы сегодня были в ударе!')
    else:
        print('Неплохой результат, но можно лучше!')

if __name__ == '__main__':
    play_guess_number()