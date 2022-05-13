import random

sentence = input("write a sentence: ")
words = sentence.split()
amount = len(words)
selected = random.randint(0, amount - 1)

print(words[selected])
