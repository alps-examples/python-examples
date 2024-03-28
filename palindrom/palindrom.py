import re

def is_palindrom(word):
    word = word.lower()
    word = re.sub('[^a-z]', '', word)
    N = len(word)
    M = N // 2  # Middle for odd, one before middle for even
    return word[0:M] == word[N-1:N-1-M:-1]
