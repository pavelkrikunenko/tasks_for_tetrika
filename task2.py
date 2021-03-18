from mwclient import Site

site = Site('ru.wikipedia.org', scheme='http')

category = site.categories['Животные_по_алфавиту']

animals = []
a = ord('А')
alphabet = list(''.join([chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)]))

for page in category:
    animals.append(page.name)

for letter in alphabet:
    counter = 0
    for animal in animals:
        if animal[0] == letter:
            counter += 1
    if counter == 0:
        continue
    print(letter + ':', counter)
