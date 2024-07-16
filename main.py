cook_book = {}

def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for i in dishes:
        for j in cook_book[i]:
            res[j['ingredient_name']] = {'measure' : j['measure'], 'quantity' : int(j['quantity']) * person_count}
    return print(res)

with open('recipes.txt', encoding='utf-8') as recept:
    for i in recept:
        dish = i[:-1]
        ingredient_quantity = int(recept.readline())
        tmp = []
        for j in range(ingredient_quantity):
            a, b, c = recept.readline().strip().split(' | ')
            tmp.append({'ingredient_name' : a, 'quantity' : b, 'measure' : c})
            cook_book[dish] = tmp
        fakeline = recept.readline()


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

file = {}

with open('sorted/1.txt', encoding='utf-8') as f1, open('sorted/2.txt', encoding='utf-8') as f2, open('sorted/3.txt', encoding='utf-8') as f3:
    tmp = []
    for i in f1:
        tmp.append(i)
    name = f1.name.split('/')
    file[name[1], len(tmp)] = tmp
    tmp = []
    for i in f2:
        tmp.append(i)
    name = f2.name.split('/')
    file[name[1], len(tmp)] = tmp
    tmp = []
    for i in f3:
        tmp.append(i)
    name = f3.name.split('/')
    file[name[1], len(tmp)] = tmp

with open('sorted/sort_files.txt', 'w', encoding='utf-8') as files:
    i = 0
    for k, v in sorted(file.items(), key=lambda x: x[1], reverse=True):
        for i in k:
            files.write(str(i) + '\n')
        n = 1
        for i in v:
            files.write(str(n) + ' ' + i)
            n += 1
        files.write('\n')
