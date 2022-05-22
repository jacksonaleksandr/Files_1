import os
from pprint import pprint
BASE_PATH = os.getcwd()
RECEIPT_FILE_NAME = "receipts.txt"

full_path = receipies = os.path.join(BASE_PATH, RECEIPT_FILE_NAME)

def receipt_dict(receipies):
    with open(receipies, "r") as file:
        cook_book = {}
        for line in file:
            line = line.strip()
            if line.isdigit() or line == "":
                continue
            elif "|" in line:
                ingredient_name, quantity, measure = map(str.strip, line.split("|"))
                cook_book[dish].append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
            else:
                dish = line
                cook_book[dish] = []

        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                ingredient, quantity, measure = ingredients
                if ingredients[ingredient] in shopping_list:
                    shopping_list[ingredients[ingredient]]['quantity'] += ingredients[quantity]*person_count
                else:
                    shopping_list[ingredients[ingredient]] = {'measure': ingredients[measure],
                                                             'quantity': ingredients[quantity]*person_count}
        else:
            print(f'{dish} нет в книге рецептов. Оно не было добавлено в список покупок')
    return shopping_list

cook_book = receipt_dict(full_path)
pprint(cook_book)
groceries = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фунчоза'], 6)
pprint(groceries)
