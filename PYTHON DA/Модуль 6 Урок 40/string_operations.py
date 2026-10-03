def count_vowels(text):
    vowels = "аеиоуыэюяАЕИОУЫЭЮЯ"
    count = 0

    for letter in text:
        if letter in vowels:
            count += 1

    return count

def reverse_string(text):
    return text[::-1]

def is_palindrome(text):
    return text == text[::-1]

def capitalize_string(text):
    words = text.split()
    new_words = []

    for word in words:
        new_words.append(word.title())

    return " ".join(new_words)