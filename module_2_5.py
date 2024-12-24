# создаем функция
def get_matrix(n, m, value):
    matrix = [] # пустой список в котором будет наша матрица
    for i in range(n): # цикл для добавления строк
        line = [] # пустой список являющийся строками в нашей матрице
        matrix.append(line)
        for j in range(m): # внутренний цикл для добавления столбцов и значений
            line.append(value) # в список "строки" добавляем значения в количестве = количеству столбцов
    return matrix # возвращаем матрицу
# проверка матрицы по значениям из примера задачи
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
# матрица по произвольно введеным значениям
result4 = get_matrix(int(input('кол-во строк: ')), int(input('кол-во столбцов: ')), int(input('значение: ')))
print(result4)