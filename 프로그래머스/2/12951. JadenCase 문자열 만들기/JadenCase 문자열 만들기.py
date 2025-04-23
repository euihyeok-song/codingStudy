def solution(s):
    words = s.split(' ')
    result = []

    for word in words:
        if word == '':
            result.append('')
        else:
            result.append(word[0].upper() + word[1:].lower() if word[0].isalpha() else word[0] + word[1:].lower())

    return ' '.join(result)