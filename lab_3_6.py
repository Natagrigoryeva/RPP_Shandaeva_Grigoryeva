import sys
print(sys.argv)
array = [float(i.replace(',','.')) for i in sys.argv if i.replace('.','',1).replace(',','',1).isdigit()]
print("Массив = ",len(array))
print(array)
print("Максимальный элемент = ", max(array))
print("Количество меньших чисел = ", sum(1 for i in array if i < max(array)))
print("Сумма чисел больших 5: ", sum(i for i in array if i > 5))
