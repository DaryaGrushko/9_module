# Генераторы

def all_variants(text):
    for w in range(len(text)):
        for k in range(len(text) - w):
            yield text[k:k + w + 1]

a = all_variants("abc")
for i in a:
    print(i)