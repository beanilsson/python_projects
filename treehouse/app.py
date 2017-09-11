def shopping_list(items):
    print('Items to purchase: ')
    for i in items:
        print(i)

def get_item():
    list = []
    item = ''
    while True:
        item = input('Enter an item, or type DONE to quit: ')
        if (item == 'DONE'):
            break
        elif (item == 'SHOW'):
            print(shopping_list(list))
            continue
        elif (item == 'HELP'):
            print('Type DONE to quit. Type SHOW to show the contents of the list. Type HELP to display this message.')
            continue
        else:
            list.append(item)

    shopping_list(list)

get_item()
