def reverse_words(s):
    reverse_string = s.split()[::-1]
    return " ".join(reverse_string)

print(">>>>>",reverse_words("aaaa bbbbb ccccc ddddd eeeee ffff"))