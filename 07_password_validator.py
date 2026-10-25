# объявление функции
def is_valid_password(password):
    password = password.split(':')
    if len(password) != 3:
        return False
    # Определяем 3 части
    a = password[0]
    b = int(password[1])
    c = int(password[2])
    # Устанавливем счетчики
    count = 0
    count_b = 0
    # Проверяем первое условие
    if a == a[::-1]:
        count += 1
    # Проверяем второе условие
    for i in range(1, b + 1):
        if b % i == 0:
            count_b += 1
            
    if count_b != 2:
        return False
    else:
        count += 1
    # Проверяем третье условие    
    if c % 2 == 0:
        count += 1
    # Проверяем общий счетчик выполненных условий    
    if count == 3:
        return True
    else:
        return False
# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))