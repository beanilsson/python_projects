def shopping_list(items):
    shopping_list = items
    print('Items to purchase: ')
    for i in items:
        print(i)

def get_item():
    item = ''
    list = []
    while True:
        item = raw_input('Enter an item, or DONE to quit ')
        if (item == 'DONE'):
            break
        else:
            list.append(item)

    shopping_list(list)

get_item()
