import sys

def caesar_shift(c, shift, base):
    if c.isalpha():
        pos = ord(c) - ord(base)
        new_pos = (pos + shift) % 26
        return chr(ord(base) + new_pos)
    return c

def encrypt_word(word):
    # Подсчитываем количество букв в слове
    length = sum(1 for c in word if c.isalpha())
    # Шифруем каждую букву сдвигом на length
    encrypted = []
    for c in word:
        if c.islower():
            encrypted.append(caesar_shift(c, length, 'a'))
        elif c.isupper():
            encrypted.append(caesar_shift(c, length, 'A'))
        else:
            encrypted.append(c)
    return ''.join(encrypted)

def main():
    input_text = sys.stdin.read().strip()
    words = input_text.split()
    encrypted_words = [encrypt_word(word) for word in words]
    output = ' '.join(encrypted_words)
    print(output)

if __name__ == "__main__":
    main()



