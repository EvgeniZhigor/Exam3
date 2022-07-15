# Задание 2
def palindrom(slovo):
    if slovo[::-1].startswith(slovo):
        return 'палиндром'
    else:
        return 'не палиндром'
slovo=input('Введите слово')
print(palindrom(slovo))
