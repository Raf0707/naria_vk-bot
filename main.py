from config import numerical_target, current_number, commnads


def input_target():
    cycle = True
    while cycle:
        try:
            numerical_target_input = int(input('Введите цель: '))
            if numerical_target_input > 0:
                cycle = False
            else:
                if numerical_target_input <= 0:
                    print('Цель не может быть меньше минимально возможного значения (1).')
        except ValueError:
            print('Введено не числовое значение.')

    setting_target = setting_a_numericial_target(numerical_target_input)
    return setting_target


def setting_a_numericial_target(numerical_target_input):
    if type(numerical_target_input) == int:
        numerical_target = numerical_target_input
    return {'num': numerical_target, 'text': f'Цель "{numerical_target}" успешно установлена!'}


def add_or_subtract_one(numerical_target, current_number, command):
    error = ''
    if command == '+ 1':
        if current_number + 1 <= numerical_target:
            current_number += 1
        else:
            error = 'Если прибавить 1, то текущее число будет больше максимально возможного (выбранной цели).'
    else:
        if current_number - 1 >= 0:
            current_number -= 1
        else:
            error = 'Если вычесть 1, то текущее число будет меньше минимально возможного (0).'
    return {'num': current_number, 'text': error}


def add_or_subtract_num(numerical_target, current_number, command):
    error = ''
    cycle = True
    while cycle:
        try:
            num = int(input('Введите число: '))
            if num > 0:
                cycle = False
            else:
                if num <= 0:
                    print('Число не может быть меньше минимально возможного значения (1).')
        except ValueError:
            print('Введено не числовое значение.')
    if command == '+ num':
        if current_number + num <= numerical_target:
            current_number += num
        else:
            error = f'Если прибавить {num}, то текущее число будет больше максимально возможного (выбранной цели).'
    else:
        if current_number - num > 0:
            current_number -= num
        else:
            error = f'Если вычесть {num}, то текущее число будет меньше минимально возможного (0).'
    return {'num': current_number, 'text': error}


def reset_target(numerical_target, current_number):
    return {'num_tar': numerical_target, 'cur_num': current_number, 'text': 'Все настройки были сброшены.'}


def main(numerical_target, current_number):
    flag = True
    target = input_target()
    numerical_target = target['num']
    print(target['text'])
    print(commnads)
    while current_number != numerical_target:
        print(f'Текущее число: {current_number}')
        command = input('Введите команду: ')
        if command in commnads:
            if command in (commnads[0], commnads[1]):
                answer = add_or_subtract_one(numerical_target, current_number, command)
                if answer['text'] == '':
                    current_number = answer['num']
                else:
                    print(answer['text'])
            if command in (commnads[2], commnads[3]):
                answer = add_or_subtract_num(numerical_target, current_number, command)
                if answer['text'] == '':
                    current_number = answer['num']
                else:
                    print(answer['text'])
            if command == 'reset':
                answer = reset_target(numerical_target, current_number)
                current_number = answer['cur_num']
                numerical_target = answer['num_tar']
                print(answer['text'])
                flag = False
                break
        else:
            print('Введена неизвестная команда.')
    if flag:
        print(f'Текущее число: {current_number}\nЦель "{numerical_target}" достигнута!')
    else:
        question = input('Хотите задать новую цель? ')
        if question == '+':
            pass
        else:
            work = False

work = True
while work:
    main(numerical_target, current_number)
