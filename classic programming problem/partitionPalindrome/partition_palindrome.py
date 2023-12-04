word = s = 'aabeggmimido'

def is_palindrome(sub):
    return False if sub != sub[::-1] else True

result = []
def backtrack(start, path):
    global result
    if start == len(word):
        result.append(path)
        return
    for end in range(start +1, len(word) + 1):
        if is_palindrome(s[start:end]):
            backtrack(end, path + [s[start:end]])

backtrack(0, [])
result[-1]