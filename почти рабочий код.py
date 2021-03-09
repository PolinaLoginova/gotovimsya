
i = 0 
a = 0 
j = 0 
b = 0
count = 0
tec_list=[''] # создаю пустую заготовку листа
new_value = '' # создаю пустую переменную 
while i < 18518:
    stroka = df.iloc[i]
    len(stroka)
    while j < len(stroka):
        if stroka[j] == ',':
            count = count + 1
        else:
            j = j + 1
    j = 0 #обнуляю перед новым циклом
    while j < len(stroka):
        if count == 21:
            if j == 8:
                continue # пропускаю запятую дроби
            if stroka[j] != ',': # если элемент не запятая, то:
                new_value = new_value + stroka[:i]  #  где i текущий номер элемента строки
                tec_list.append(new_value) # записываю в переменную "слово"
                j = j + 1
            if stroka[j] == ',': #если символ равен запятой, начинает твориться экшееееен
                 tec_list.append(new_value)
                 new_value.clear
                 j = j + 1
        if count == 20:
            if stroka[j] != ',': # если элемент не запятая, то:
                new_value = new_value + stroka[:i]  #  где i текущий номер элемента строки
                tec_list.append(new_value) # записываю в переменную "слово"
                j = j + 1
            if stroka[j] == ',': #если символ равен запятой, начинает твориться экшееееен
                 tec_list.append(new_value)
                 new_value.clear
                 j = j + 1
