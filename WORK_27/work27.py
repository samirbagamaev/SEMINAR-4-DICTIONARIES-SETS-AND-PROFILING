# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# Output: 13

text = input('введите текст: ').split()
words=set()
for i in text:
        words.add(i)
    
print(len(words))

#или же так


stroka = input().lower().split()
print(type(stroka))
print(stroka)
result = set(stroka)
print(len(result))
