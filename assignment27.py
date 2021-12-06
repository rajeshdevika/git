a = ['a', 'e', 'i', 'o', 'u']
b = ['@', '#', '$', '%', '*']
count = 0
special = 0
consonants = 0
digits = 0
w = input('enter: ').strip()
print(w)
for j in w:
    if (j in a):
        count += 1
    elif (j in b):
        special += 1
    elif (j.isdigit()):
        digits += 1
    elif (j not in a) and (j != ' '):
        consonants += 1

print('count of vowels:', (count))
print('count of special:', (special))
print('count of consonants:', (consonants))
print('count of digit:', (digits))