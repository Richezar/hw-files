my_cook_book = {}
from copy import deepcopy
import os
def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    cook_book = deepcopy(my_cook_book)
    for i in dishes:
        if i in cook_book:
            for j in cook_book[i]:
                j['quantity'] *= person_count
                res[j['ingredient_name']] = j
        else:
            print(f'Блюда {i} нет в рецептах')
    return print(res)

with open('recipes.txt', encoding='utf-8') as recept:
    for i in recept:
        dish = i[:-1]
        ingredient_quantity = int(recept.readline())
        tmp = []
        for j in range(ingredient_quantity):
            a, b, c = recept.readline().strip().split(' | ')
            tmp.append({'ingredient_name' : a, 'quantity' : int(b), 'measure' : c})
            my_cook_book[dish] = tmp
        fakeline = recept.readline()


get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)

file = {}
for filename in sorted(os.listdir('sorted'), key=len):
    with open(f'sorted/{filename}', encoding='utf-8') as f:
        tmp = []
        for i in f:
            tmp.append(i)
        file[filename, len(tmp)] = tmp

with open('sort_files.txt', 'w', encoding='utf-8') as files:
    for k, v in sorted(file.items(), key=lambda x: x[1], reverse=True):
        for i in k:
            files.write(str(i) + '\n')
        n = 1
        for i in v:
            files.write(str(n) + ' ' + i)
            n += 1
        files.write('\n')

