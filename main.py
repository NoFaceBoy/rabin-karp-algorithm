alphabet_size = 256


def rabin_karp_search(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    prime_number = 61
    text_hash_value = 0
    pattern_hash_value = 0
    current_hash_value = 1
    occurrences = []

    for i in range(pattern_length):
        text_hash_value = (alphabet_size * text_hash_value + ord(text[i])) % prime_number
        pattern_hash_value = (alphabet_size * pattern_hash_value + ord(pattern[i])) % prime_number

    for i in range(pattern_length - 1):
        current_hash_value = (current_hash_value * alphabet_size) % prime_number

    for i in range(text_length - pattern_length + 1):
        if pattern_hash_value == text_hash_value:
            occurrences_number = 0
            for j in range(pattern_length):
                if pattern[j] == text[j + i]:
                    occurrences_number += 1
                else:
                    break
            if occurrences_number == pattern_length:
                occurrences.append(i)

        if i < text_length - pattern_length:
            text_hash_value = (alphabet_size * (text_hash_value - ord(text[i]) * current_hash_value) + ord(
                text[i + pattern_length])) % prime_number

            if text_hash_value < 0:
                text_hash_value += prime_number
    return occurrences