
# Задача 1
def create_cook_book('Recept.txt'):
    cook_book = {}
    try:
        with open('Recept.txt', encoding='utf-8') as f:
            ingredients_list = [line.strip() for line in f]
        for  i, c in enumerate(list):
            if c.isdigit():
                cook_book[list[i - 1]] = []
                for slice in list[i + 1:i + int(c) + 1]:
                    ingredient_name = slice.split('|')[0]
                    quantity = int(slice.split('|')[1])
                    measure = slice.split('|')[2]
                    cook_book[list[i - 1]].append({'ingredient_name': ingredient_name,
                                                  'quantity': quantity,
                                                  'measure': measure})
        return cook_book
    except FileNotFoundError:
        return (f'Файл не найден.')
    except Exception as error:
        return f'Ошибка'

print()
print(create_cook_book('Recept.txt'))
print()
print()

# Задача 2
def get_shop_list_by_dishes(dishes, cooking_book, person_count):
    ing_dict = {}

    for key in cooking_book.keys ():
        for dish in dishes:
            if key == dish:
                for dictionary in cooking_book[key]:
                    ing_name = dictionary['ingredient_name']
                    try:
                        ing_dict[ing_name]['quantity'] += (dictionary['quantity'] * person_count)
                    except:
                        ing_dict[ing_name] = {'measure': dictionary['measure'],
                                              'quantity': dictionary['quantity'] * person_count}
    return ing_dict

print()
print(get_shop_list_by_dishes(['Омлет', 'Омлет'], create_cook_book('Recept.txt'), 2))
print()
print()

