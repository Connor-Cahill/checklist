checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    if index <= len(checklist):
        print(checklist[index])
        return checklist[index]
    else:
        print('no item in list index')

def update(index, item):
    if index <= len(checklist):
        checklist[index] = item
    else:
        print('no item in checklist index')

def destroy(index):
    if index <= len(checklist):
        checklist.pop(index)
    else:
         print('no item in checklist index')

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(str(index), list_item))
        index += 1

def mark_completed(index):
    checklist[index] = '√ ' + checklist[index]

def select(function_code):
    #create item
    if function_code == 'C' or function_code == 'c':
        input_item = user_input('Input Item: ')
        create(input_item)
        return True

    elif function_code == 'R' or function_code == 'r':
        index = int(user_input("Index Number?"))
        read(index)
        return True
    elif function_code == 'P' or function_code == 'p':
        list_all_items()
        return True
    elif function_code == 'Q' or function_code == 'q':
        return False
    elif function_code == 'D' or function_code == 'd':
        index = int(user_input('Index Number?'))
        destroy(index)
    elif function_code == 'U' or function_code == 'u':
        index = int(user_input('Index Number?'))
        item = user_input('Updated Item: ')
        update(index, item)
    elif function_code == 'M' or function_code == 'm':
        index = int(user_input('Index Number?'))
        mark_completed(index)
    else:
        print('Unknown Option')
        return True

def user_input(prompt):
    #displays message in terminal and waits for user response
    user_input = input(prompt)
    return user_input

running = True
while running:
    selection = user_input('Press C to add to list-- R to read from list -- P to display list -- D to delete item -- U to update and item -- M to mark an item completed -- AND Q to quit: ')
    select(selection)



def test():
    create('purple sox')
    create('red cloake')

    print(read(0))
    print(read(1))

    update(0, 'purple socks')
    destroy(1)

    print(read(0))
    #print(read(1))
    create('Yellow Shoes')
    mark_completed(1)
    print(read(1))

    select('C')
    list_all_items()
    select('R')
    list_all_items()
    user_value = user_input('Please Enter a Value:')
    print(user_value)




test()


# create('Blue')
# create('Orange')
