# Задание 1
print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 3))
print(type(15 ** 3))

#Задание 2
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
           'была', '+5', 'градусов']

new_list = []
for idx, elem in enumerate(my_list):
    if elem.isdigit():
        new_list.extend(['"', f'{int(elem):02}', '"'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
        new_list.extend(['"', f'{elem[0]}{int(elem):02}', '"'])
    else:
        new_list.append(elem)

out_info = ' '.join(new_list)
print(out_info)


symbol_idxs = []
for idx, letter in enumerate(out_info):
    if letter == '"':
        symbol_idxs.append(idx)


for idx in range(len(symbol_idxs)):
    if idx % 2 == 0:
        symbol_idxs[idx] = symbol_idxs[idx] + 1
    else:
        symbol_idxs[idx] = symbol_idxs[idx] - 1


for del_idx in reversed(symbol_idxs):
    out_info = out_info[:del_idx] + out_info[del_idx+1:]

#Задание 4
bad_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
            'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for position in bad_list:
    print('Привет', position.split()[-1].title())