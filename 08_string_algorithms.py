# 12_string_algorithms.py

def is_correct_bracket(text: str) -> bool:
    """Проверка правильности расстановки скобок."""
    count = 0
    for char in text:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0


def is_palindrome(text: str) -> bool:
    """Проверка, является ли строка палиндромом (без учета регистра и знаков)."""
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def is_one_away(word1: str, word2: str) -> bool:
    """Проверяет, отличаются ли слова ровно на одну букву."""
    if word1 == word2 or len(word1) != len(word2):
        return False
    
    diff_count = sum(1 for i in range(len(word1)) if word1[i] != word2[i])
    return diff_count == 1


def convert_to_python_case(text: str) -> str:
    """Преобразование CamelCase в snake_case."""
    new_text = text[0].lower()
    for char in text[1:]:
        if char.isupper():
            new_text += '_' + char.lower()
        else:
            new_text += char
    return new_text


def find_all(target: str, symbol: str) -> list:
    """Возвращает список всех индексов вхождения символа."""
    indices = []
    start = 0
    while True:
        index = target.find(symbol, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1
    return indices


if __name__ == '__main__':
    # Примеры использования
    print("Скобки (()()):", is_correct_bracket("(()())"))
    print("Палиндром (А роза упала на лапу Азора):", is_palindrome("А роза упала на лапу Азора"))
    print("Разница в одну букву (кот, код):", is_one_away("кот", "код"))
    print("В snake_case (CamelCaseText):", convert_to_python_case("CamelCaseText"))
    print("Индексы 'а' в слове 'абракадабра':", find_all("абракадабра", "а"))