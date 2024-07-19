import os
def create_cook_book():
    res = {}
    with open('recipes.txt', encoding='utf-8') as recept:
        for i in recept:
            dish = i[:-1]
            ingredient_quantity = int(recept.readline())
            tmp = []
            for j in range(ingredient_quantity):
                a, b, c = recept.readline().strip().split(' | ')
                tmp.append({'ingredient_name' : a, 'quantity' : int(b), 'measure' : c})
                res[dish] = tmp
            fakeline = recept.readline()
        return res

def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    cook_book = create_cook_book()
    for i in dishes:
        if i in cook_book:
            for j in cook_book[i]:
                j['quantity'] *= person_count
                res[j['ingredient_name']] = j
        else:
            print(f'Блюда {i} нет в рецептах')
    return print(res)

get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)
get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)

def reading_all_files():
    res = {}
    for filename in sorted(os.listdir('sorted'), key=len):
        with open(f'sorted/{filename}', encoding='utf-8') as f:
            tmp = []
            for i in f:
                tmp.append(i)
            res[filename, len(tmp)] = tmp
    return res

def sorted_all_files():
    with open('sort_files.txt', 'w', encoding='utf-8') as files:
        for k, v in sorted(reading_all_files().items(), key=lambda x: x[1], reverse=True):
            for i in k:
                files.write(str(i) + '\n')
            n = 1
            for i in v:
                files.write(str(n) + ' ' + i)
                n += 1
            files.write('\n')

sorted_all_files()
